import time
import concurrent.futures
import requests
import json
import ast
import re
import os
import ollama

# SET ENVIRONMENT VARIABLES ON YOUR PC OR REPLACE THE OS.GETENV() WITH YOUR API KEYS AS STRINGS
GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH")  # Replace with your Google Search API key
GOOGLE_CSE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")  # Replace with your Custom Search Engine ID

# Select models for tasks
RESEARCH_MODEL = "llama3"
REPORT_MODEL = "llama3"  # set the model which will generate the final comprehensive report

# Set the pause duration in seconds
PAUSE_DURATION = 1

def remove_first_line(test_string):
    if test_string.startswith("Here") and test_string.split("\n")[0].strip().endswith(":"):
        return re.sub(r'^.*\n', '', test_string, count=1)
    return test_string

def generate_text(prompt, model):
    try:
        stream = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a world-class researcher. Analyze the given information and generate a detailed, comprehensive, and well-structured report."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            stream=True,
        )
        response_text = ""
        for chunk in stream:
            response_text += chunk['message']['content']
        print(remove_first_line(response_text.strip()))
        return remove_first_line(response_text.strip())
    except Exception as e:
        raise Exception(f"Request failed: {e}")

def search_web(search_term, api_key, cse_id):
    try:
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_term}"
        response = requests.get(url)
        result = response.json()
        relevant_text = []
        for item in result['items']:
            title = item['title']
            snippet = item.get('snippet', '')  # Use get() to handle missing 'snippet' key
            relevant_text.append(f"Title: {title}\nSnippet: {snippet}\n")
        print("\n".join(relevant_text))
        return relevant_text
    except Exception as e:
        print(f"Error occurred during web search: {e}")
        return []

def generate_subtopic_report(research_topic, subtopic):
    search_data = []
    all_queries = []
    search_cache = {}
    print(f"Generating initial search queries for subtopic: {subtopic}...")
    initial_queries_prompt = f"Generate 5 search queries to gather information on the subtopic '{subtopic}' of the research topic '{research_topic}'. Return your queries in a Python-parseable list. Return nothing but the list. Do so in one line. Start your response with [\""
 
    initial_queries_response = generate_text(initial_queries_prompt, model=RESEARCH_MODEL)
    if initial_queries_response.startswith('[') and ']' in initial_queries_response:
        try:
            initial_queries = ast.literal_eval(initial_queries_response)
        except SyntaxError:
            print("Error: Invalid search query format. Skipping initial queries.")
            initial_queries = []
    else:
        print("Error: Search query format not found. Skipping initial queries.")
        initial_queries = []
   
    print(initial_queries)
    all_queries.extend(initial_queries)
    def search_and_cache(query):
        if query in search_cache:
            return search_cache[query]
        else:
            search_results = search_web(query, GOOGLE_API_KEY, GOOGLE_CSE_ID)
            search_cache[query] = search_results
            return search_results
    with concurrent.futures.ThreadPoolExecutor() as executor:
        search_results = list(executor.map(search_and_cache, initial_queries))
        search_data.extend(search_results)
 
    print(f"Generating initial report for subtopic: {subtopic}...")
    report_prompt = f"When writing your report, make it incredibly detailed, thorough, specific, and well-structured. Use Markdown for formatting. Analyze the following search data and generate a comprehensive report on the subtopic '{subtopic}' of the research topic '{research_topic}':\n\n{str(search_data)}"
    report = generate_text(report_prompt, model=RESEARCH_MODEL)
    print(f"Analyzing report and generating additional searches for subtopic: {subtopic}...")
    analysis_prompt = f"Analyze the following report on the subtopic '{subtopic}' of the research topic '{research_topic}' and identify areas that need more detail or further information:\n\n{report}\n\n---\n\nHere are all the search queries you have used so far for this subtopic:\n\n{str(all_queries)}\n\n---\n\nGenerate 5 new and unique search queries to fill in the gaps and provide more detail on the identified areas. Return your queries in a Python-parseable list. Return nothing but the list. Do so in one line. Start your response with [\""
   
    additional_queries_response = generate_text(analysis_prompt, model=RESEARCH_MODEL)
    if additional_queries_response.startswith('[') and ']' in additional_queries_response:
        try:
            additional_queries = ast.literal_eval(additional_queries_response)
        except SyntaxError:
            print("Error: Invalid search query format. Skipping additional queries.")
            additional_queries = []
    else:
        print("Error: Search query format not found. Skipping additional queries.")
        additional_queries = []
   
    all_queries.extend(additional_queries)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        additional_search_results = list(executor.map(search_and_cache, additional_queries))
        search_data.extend(additional_search_results)
    print(f"Updating report with additional information for subtopic: {subtopic}...")
    update_prompt = f"Update the following report on the subtopic '{subtopic}' of the research topic '{research_topic}' by incorporating the new information from the additional searches. Keep all existing information... only add new information:\n\n{report}\n\n---\n\nAdditional search data:\n\n{str(additional_search_results)}\n\n---\n\nGenerate an updated report that includes the new information and provides more detail in the identified areas. Use Markdown for formatting."
    report = generate_text(update_prompt, model=RESEARCH_MODEL)
    print(f"Final report generated for subtopic: {subtopic}!")
    return report

def generate_comprehensive_report(research_topic, subtopic_reports):
    print("Generating comprehensive report...")
    comprehensive_report_prompt = f"Generate a comprehensive report on the research topic '{research_topic}' by combining the following reports on various subtopics:\n\n{subtopic_reports}\n\n---\n\nEnsure that the final report uses markdown formatting, and is very detailed, well-structured and covers all of the gathered information about the subtopics. Make sure you do your best not to repeat duplicate information between each of the subtopics. Nothing -- absolutely nothing, should be left out. The final report should contain a SINGLE '### Conclusion' at the end of the full comprehensive report. If you forget to include ANY information from any of the previous reports that aren't redundant, if you include more than a SINGLE '### Conclusion' section, or if the '### Conclusion' is not at the very end of the report, you will face the consequences. Include a table of contents. Leave nothing out. Use Markdown for formatting."
    comprehensive_report = generate_text(comprehensive_report_prompt, model=REPORT_MODEL)
   
    # Check if the report is cut short and generate additional content if needed
    while "### Conclusion" not in comprehensive_report:
        print("Report is cut short. Generating additional content...")
        continuation_prompt = f"The comprehensive report is cut short. Please continue generating the report from where it left off. Here's the current report:\n\n{comprehensive_report}\n\n---\n\nContinue the report seamlessly from the point you left off, and continue ensuring that all key information from the subtopic reports is included and that the report is well-structured and comprehensive. Use Markdown for formatting."
        additional_content = generate_text(continuation_prompt, model=REPORT_MODEL)
        comprehensive_report += "\n\n" + additional_content
   
    print("Comprehensive report generated!")
    return comprehensive_report

# User input
research_topic = input("Enter the research topic: ")

# Generate subtopic checklist
subtopic_checklist_prompt = f"Generate a detailed checklist of subtopics to research for the topic '{research_topic}'. Return your checklist in a Python-parseable list. Return nothing but the list. Do so in one line. Maximum five sub-topics. Start your response with [\""
subtopic_checklist = ast.literal_eval('[' + generate_text(subtopic_checklist_prompt, model=RESEARCH_MODEL).split('[')[1])
print(f"Subtopic Checklist: {subtopic_checklist}")

# Pause after receiving the generated subtopics
print(f"Pausing for {PAUSE_DURATION} seconds...")
time.sleep(PAUSE_DURATION)

# Generate reports for each subtopic
subtopic_reports = []
for subtopic in subtopic_checklist:
    subtopic_report = generate_subtopic_report(research_topic, subtopic)
    subtopic_reports.append(subtopic_report)

# Pause after receiving the generated subtopic reports
print(f"Pausing for {PAUSE_DURATION} seconds...")
time.sleep(PAUSE_DURATION)

# Combine subtopic reports into a comprehensive report
comprehensive_report = generate_comprehensive_report(research_topic, "\n\n".join(subtopic_reports))

# Pause after creating the chunks of the comprehensive report
print(f"Pausing for {PAUSE_DURATION} seconds...")
time.sleep(PAUSE_DURATION)

# Create the "reports" directory if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Save the comprehensive report to a file with the format "[research_topic]_report.md" in the "reports" directory
report_filename = f"{research_topic.replace(' ', '_')}_report.md"
report_filepath = os.path.join("reports", report_filename)
try:
    with open(report_filepath, "w", encoding="utf-8") as file:
        file.write(comprehensive_report)
    print(f"Comprehensive report saved as '{report_filepath}'.")
except UnicodeEncodeError as e:
    print(f"Error: Unable to save the report due to unsupported characters. Please try again with a different research topic or modify the generated report to remove any unsupported characters.")
    print(f"Error details: {e}")