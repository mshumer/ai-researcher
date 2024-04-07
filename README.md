# Fork of [AI-Researcher](https://github.com/mshumer/ai-researcher) by [@mattshumer](https://github.com/mshumer)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1G6GA2Od-x_cf-xt0B5jOz0Me-bBAsXVz?usp=sharing)

This project is an evolving fork of the `ai-researcher` repository originally created by [@mattshumer](https://github.com/mshumer). The original version utilized Claude 3 and SERPAPI to conduct research. This fork modifies the original project to use Google Search API for searching capabilities. Below are the details of the modifications:
Changes will be taking place quite a bit, but pushed updates may be sparse depending on free personal time

# Notice:
1. **The OAI_Researcher_Google_API.ipynb book was added, from [Jorskalz's OpenAI-Researcher](https://github.com/joriskalz/ai-researcher)**
   
   Decided to refrain from creating a fork of the fork of the fork... but used it as the basis to recreate my book, [Claude_Researcher_Google_API.ipynb](https://github.com/Binxly/ai-researcher/blob/main/Claude_Researcher_Google_API.ipynb)
   
## Changes Made

1. **Google Search API Integration**: The script now uses the Google Custom Search API to perform web searches instead of the SERP API. This allows for more reliable and accurate search results.

2. **Concurrent Search Requests**: The script utilizes concurrent.futures to perform multiple search requests simultaneously, improving the overall speed and efficiency of the research process.

3. **Search Result Caching**: A search cache has been implemented to store the results of previous searches. This prevents redundant API calls and speeds up the research process by reusing cached results when possible.

4. **Anthropic API Client**: The script now uses the official Anthropic API client library (anthropic) for a more reliable and efficient interaction with the Anthropic API.

5. **Configurable Models**: The script allows you to select different models for the research and report generation tasks. You can set the `RESEARCH_MODEL` and `REPORT_MODEL` variables to choose the desired models for each task.

6. **Environment Variables**: API keys and other sensitive information are now stored as environment variables. You can set the `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, and `GOOGLE_CSE_ID` variables in your environment or replace the `os.getenv()` calls with your actual API keys.

7. **Error Handling**: Improved error handling has been added throughout the script to gracefully handle and report any errors that may occur during the research and report generation process.

8. **Markdown Formatting**: The generated reports are now formatted using Markdown, making them more readable and visually appealing.

9. **Report Continuation**: If the generated comprehensive report is cut short, the script will automatically generate additional content to ensure a complete and comprehensive report.

10. **Saving Reports**: The generated comprehensive report is now saved in a dedicated "reports" directory with a filename based on the research topic. The script handles the creation of the directory if it doesn't exist.

## Usage

To use the Comprehensive Research Report Generator:

1. Set up your environment variables or replace the `os.getenv()` calls with your actual API keys.
2. Run the script and enter your desired research topic when prompted.
3. The script will generate a subtopic checklist, perform research on each subtopic, and generate individual subtopic reports.
4. Finally, it will combine the subtopic reports into a comprehensive report and save it as a Markdown file in the "reports" directory.

Note: The script uses the Anthropic API and Google Custom Search API, which may incur costs based on usage. Please review the pricing and usage limits of these APIs before running the script.

## Acknowledgements

Credit goes to the original creator, [@mattshumer](https://github.com/mshumer), for the foundational work on the `ai-researcher`. The enhancements made in this fork aim to build upon the original project while adapting it for Google Search API integration.

## Notice of Modifications

This document outlines the changes from the original project. It should be noted that while the core functionality remains the same, the search process is now tailored to work with the Google Search API. These modifications should improve the efficiency and potentially the effectiveness of the AI Researcher tool.

---
This document is for the forked project and should be used in conjunction with the original project's documentation for a complete understanding of the system's capabilities and usage.
