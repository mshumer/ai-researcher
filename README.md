# Fork of [AI-Researcher](https://github.com/mshumer/ai-researcher) by [@mattshumer](https://github.com/mshumer)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1G6GA2Od-x_cf-xt0B5jOz0Me-bBAsXVz?usp=sharing)

This project is an evolving fork of the `ai-researcher` repository originally created by [@mattshumer](https://github.com/mshumer). The original version utilized Claude 3 and SERPAPI to conduct research. This fork modifies the original project to use Google Search API for searching capabilities. Below are the details of the modifications:
Changes will be taking place quite a bit, but pushed updates may be sparse depending on free personal time

## Changes Made

1. **Library Replacement**:
   The `serpapi` library has been replaced with the `google-api-python-client` library. To install the new library, use the following command:

   ```shell
   !pip install google-api-python-client
   ```

2. **Function Update**:
   The `search_web` function has been updated to leverage the Google Search API:

   ```python
   from googleapiclient.discovery import build

   def search_web(search_term, api_key, cse_id):
       service = build("customsearch", "v1", developerKey=api_key)
       result = service.cse().list(q=search_term, cx=cse_id).execute()
       return result
   ```

3. **Configuration Update**:
   The environment variables for API keys have been updated to use Google's infrastructure:

   ```python
   GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
   GOOGLE_CSE_ID = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
   ```

4. **API Call Update**:
   All calls to `search_web` have been updated to include the Google Search API key and Custom Search Engine ID:

   ```python
   search_results = search_web(query, GOOGLE_API_KEY, GOOGLE_CSE_ID)
   ```

5. **Code Optimization**:
   To enhance efficiency, the following optimizations were made:
   - The number of API calls has been reduced by executing a single round of more targeted searches.
   - The generation of search queries in each round has been adjusted to improve the quality and relevance of results.

6. **Concurrency Implementation**:
   Concurrent requests have been enabled using the `concurrent.futures` module, significantly speeding up the search process.

7. **Caching Implementation**:
   A caching mechanism has been added to store and reuse search results, minimizing redundant API calls.

## Acknowledgements

Credit goes to the original creator, [@mattshumer](https://github.com/mshumer), for the foundational work on the `ai-researcher`. The enhancements made in this fork aim to build upon the original project while adapting it for Google Search API integration.

## Notice of Modifications

This document outlines the changes from the original project. It should be noted that while the core functionality remains the same, the search process is now tailored to work with the Google Search API. These modifications should improve the efficiency and potentially the effectiveness of the AI Researcher tool.

---
This document is for the forked project and should be used in conjunction with the original project's documentation for a complete understanding of the system's capabilities and usage.
