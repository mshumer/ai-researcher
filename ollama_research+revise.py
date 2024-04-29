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
RESEARCH_MODEL = "llama3:8b-instruct-fp16"
REPORT_MODEL = "llama3:8b-instruct-fp16"  # set the model which will generate the final comprehensive report

# Example report format
EXAMPLE_REPORT_FORMAT = """
# Table of Contents

1. [Introduction](#introduction)
2. [Section 1](#section-1)
    - [Subsection 1](#subsection-1)
    - [Subsection 2](#subsection-2)
    - [Subsection 3](#subsection-3)
3. [Section 2](#section-2)
    - [Subsection 1](#subsection-1-1)
    - [Subsection 2](#subsection-2-1)
4. [Section 3](#section-3)
    - [Subsection 1](#subsection-1-2)
5. [Section 4](#section-4)
    - [Subsection 1](#subsection-1-3)
6. [Section 5](#section-5)
    - [Subsection 1](#subsection-1-4)
    - [Subsection 2](#subsection-2-2)
7. [Section 6](#section-6)
    - [Subsection 1](#subsection-1-5)
    - [Subsection 2](#subsection-2-3)
8. [Section 7](#section-7)
    - [Subsection 1](#subsection-1-6)
    - [Subsection 2](#subsection-2-4)
9. [Section 8](#section-8)
10. [Conclusion](#conclusion)

## Introduction

[Report continues from here, including all 10 sections...]
"""

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
    comprehensive_report_prompt = f"Generate a comprehensive report on the research topic '{research_topic}' by combining the following reports on various subtopics:\n\n{subtopic_reports}\n\n---\n\nEnsure that the final report follows the format provided in this example report:\n\n{EXAMPLE_REPORT_FORMAT}\n\nMake sure the report is very detailed, well-structured, and covers all of the gathered information about the subtopics. Avoid repeating duplicate information between each of the subtopics. Nothing should be left out. Include a single '## Conclusion' section at the end of the report. If you forget to include any information from the previous reports that aren't redundant, if you include more than a single '## Conclusion' section, or if the '## Conclusion' is not at the very end of the report, you will face consequences. Include a table of contents. Leave nothing out. Use Markdown for formatting."
    comprehensive_report = generate_text(comprehensive_report_prompt, model=REPORT_MODEL)
   
    # Check if the report is cut short and generate additional content if needed
    while "## Conclusion" not in comprehensive_report:
        print("Report is cut short. Generating additional content...")
        continuation_prompt = f"The comprehensive report is cut short. Please continue generating the report from where it left off. Here's the current report:\n\n{comprehensive_report}\n\n---\n\nContinue the report seamlessly from the point you left off, and continue ensuring that all key information from the subtopic reports is included and that the report follows the format provided in this example report:\n\n{EXAMPLE_REPORT_FORMAT}\n\nMake sure the report is well-structured and comprehensive. Use Markdown for formatting."
        additional_content = generate_text(continuation_prompt, model=REPORT_MODEL)
        comprehensive_report += "\n\n" + additional_content
   
    print("Comprehensive report generated!")
    return comprehensive_report

def revise_report(research_report):
    search_data = []
    all_queries = []
    search_cache = {}

    print("Analyzing report and generating search queries...")
    analysis_prompt = f"Analyze the following research report and identify areas of the report that need more detail or further information:\n\n{research_report}\n\n---\n\nGenerate 5 search queries to gather additional information to enhance the report. Return your queries in a Python-parseable list. Return nothing but the list. Do so in one line. Start your response with [\""
    queries_response = generate_text(analysis_prompt, model=RESEARCH_MODEL)

    if queries_response.startswith('[') and ']' in queries_response:
        try:
            queries = ast.literal_eval(queries_response)
        except SyntaxError:
            print("Error: Invalid search query format. Skipping queries.")
            queries = []
    else:
        print("Error: Search query format not found. Skipping queries.")
        queries = []

    all_queries.extend(queries)

    def search_and_cache(query):
        if query in search_cache:
            return search_cache[query]
        else:
            search_results = search_web(query, GOOGLE_API_KEY, GOOGLE_CSE_ID)
            search_cache[query] = search_results
            return search_results

    with concurrent.futures.ThreadPoolExecutor() as executor:
        search_results = list(executor.map(search_and_cache, queries))
        search_data.extend(search_results)

    print("Updating report with additional information...")
    update_prompt = f"Update the following research report by incorporating the new information from the searches. Additionally, identify areas of the report which are redundant/duplicate areas of information, and make necessary changes to the verbiage as needed in order to get points across better. However, avoid using hyperbole or terms of grandeur. The goal is to improve this report:\n\n{research_report}\n\n---\n\nAdditional search data:\n\n{str(search_data)}\n\n---\n\nGenerate an updated report that includes the new information and provides more detail in the identified areas. Remember to revise the Table of Contents as needed. Use Markdown for formatting."
    updated_report = generate_text(update_prompt, model=REPORT_MODEL)
    print("Report revision completed!")
    return updated_report

# User input
research_topic = input("Enter the research topic: ")

# Generate subtopic checklist
subtopic_checklist_prompt = f"Generate a detailed checklist of subtopics to research for the topic '{research_topic}'. Return your checklist in a Python-parseable list. Return nothing but the list. Do so in one line. Maximum five sub-topics. Start your response with [\""
subtopic_checklist = ast.literal_eval('[' + generate_text(subtopic_checklist_prompt, model=RESEARCH_MODEL).split('[')[1])
print(f"Subtopic Checklist: {subtopic_checklist}")

# Generate reports for each subtopic
subtopic_reports = []
for subtopic in subtopic_checklist:
    subtopic_report = generate_subtopic_report(research_topic, subtopic)
    subtopic_reports.append(subtopic_report)

# Combine subtopic reports into a comprehensive report
comprehensive_report = generate_comprehensive_report(research_topic, "\n\n".join(subtopic_reports))

# Create the "reports" directory if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Save the comprehensive report before revision
report_filename_before_revision = f"{research_topic.replace(' ', '_')}_report_before_revision.md"
report_filepath_before_revision = os.path.join("reports", report_filename_before_revision)
try:
    with open(report_filepath_before_revision, "w", encoding="utf-8") as file:
        file.write(comprehensive_report)
    print(f"Comprehensive report before revision saved as '{report_filepath_before_revision}'.")
except UnicodeEncodeError as e:
    print(f"Error: Unable to save the report before revision due to unsupported characters. Please try again with a different research topic or modify the generated report to remove any unsupported characters.")
    print(f"Error details: {e}")

# Revise the comprehensive report
revised_report = revise_report(comprehensive_report)

# Save the revised report to a file with the format "[research_topic]_report_revised.md" in the "reports" directory
report_filename_revised = f"{research_topic.replace(' ', '_')}_report_revised.md"
report_filepath_revised = os.path.join("reports", report_filename_revised)
try:
    with open(report_filepath_revised, "w", encoding="utf-8") as file:
        file.write(revised_report)
    print(f"Revised report saved as '{report_filepath_revised}'.")
except UnicodeEncodeError as e:
    print(f"Error: Unable to save the revised report due to unsupported characters. Please try again with a different research topic or modify the generated report to remove any unsupported characters.")
    print(f"Error details: {e}")