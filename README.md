<<<<<<< Updated upstream
# ai-researcher
[![Twitter Follow](https://img.shields.io/twitter/follow/mattshumer_?style=social)](https://twitter.com/mattshumer_) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fn2Xisstp0d30_bAaLPA1y-0_svojLF3?usp=sharing)

The AI Researcher is an AI agent that utilizes Claude 3 and SERPAPI to perform comprehensive research on a given topic. It breaks down the research process into subtopics, generates individual reports for each subtopic, and then combines them into a final comprehensive report.

## *New 4/9/24: The Gemini 1.5 Pro | YouTube Researcher Version*
I've added a new version of ai-researcher that takes advantage of Google's Gemini 1.5 Pro model. This version listens to a set of YouTube videos about a specific topic and creates a report based on their contents. Try it out with the `Gemini_Youtube_Researcher.ipynb` notebook in the repo!

## Features

- Generates a detailed checklist of subtopics to research for a given topic
- Performs multiple rounds of searches and analysis for each subtopic
- Generates individual reports for each subtopic
- Incorporates feedback from a "boss" persona to identify missing information and improve the reports
- Combines the subtopic reports into a comprehensive final report
=======
# AI Research Assistants

This repository contains a variety of AI-assisted research tools and sub-agent pipelines designed to aid in various tasks.

## Table of Contents

- [Introduction](#introduction)
- [Acknowledgements](#acknowledgements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Folder Structure](#folder-structure)
  - [Notebooks](#notebooks)
  - [reports](#reports)
  - [Scripts](#scripts)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a variety of AI-assisted research tools and sub-agent pipelines designed to aid in different tasks. The tools are organized into different folders based on their types.

# Acknowledgements

This project is an evolving fork of the [AI-Researcher](https://github.com/mshumer/ai-researcher) repository originally created by [@mattshumer](https://github.com/mshumer). The original version utilized Claude 3 and SERPAPI to conduct research. This fork modifies the original project to encompass an array of agent+sub-agent pipelines, including real-time research and comprehensive report creation/revision.
Changes will be taking place quite a bit, but pushed updates may be sparse depending on free personal time

## Installation

To use the tools in this repository, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/AI-Research-Assistants.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Environment Variables

The following environment variables are used in the scripts and notebooks:

- `ANTHROPIC_API_KEY`: API key for accessing the Anthropic API.
- `GOOGLE_SEARCH`: API key for accessing the Google Search API.
- `GOOGLE_SEARCH_ENGINE_ID`: Search engine ID for the Google Custom Search API.

Make sure to set these environment variables or replace the `os.getenv()` calls with your actual API keys before running the scripts or notebooks.

## Folder Structure

### Notebooks
>>>>>>> Stashed changes

This folder contains Jupyter notebooks used for various research and sub-agent tasks.
Documentation provided in the books.

<<<<<<< Updated upstream
1. [Open the notebook in Google Colab](https://colab.research.google.com/drive/1fn2Xisstp0d30_bAaLPA1y-0_svojLF3?usp=sharing) or in a local Jupyter notebook.

2. Replace the placeholders `ANTHROPIC_API_KEY` and `SERP_API_KEY` in the script with your actual API keys.

3. Run all the cells, and enter your topic to get started!

4. After research + generation is complete, the report will be saved as `comprehensive_report.txt` in the same directory as the script. Use a Markdown viewer to view the final report.

## Customization

You can customize the behavior of the AI Research Assistant by modifying the following parameters in the script:

- `model`: The name of the Anthropic Claude AI model to use (default: "claude-3-haiku-20240307").
- `max_tokens`: The maximum number of tokens to generate in each AI response (default: 2000).
- `temperature`: The temperature value for controlling the randomness of the AI responses (default: 0.7).

## Limitations

- The quality and accuracy of the generated reports depend on the performance of the Anthropic Claude AI and the relevance of the search results from SERPAPI.
- The script may take a considerable amount of time to execute, especially for complex topics with multiple subtopics.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

The AI Research Assistant is an experimental tool and should be used for informational purposes only. The generated reports may contain inaccuracies or inconsistencies. Always verify the information obtained from the script with reliable sources before making any decisions based on it.

## Contributing

Contributions to the AI Research Assistant are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## Acknowledgments

- [Anthropic](https://www.anthropic.com/) for providing the Claude AI API.
- [SERPAPI](https://serpapi.com/) for providing the search API.

## Contact

Matt Shumer - [@mattshumer_](https://twitter.com/mattshumer_)

Lastly, if you want to try something even cooler than this, sign up for [HyperWrite Personal Assistant](https://app.hyperwriteai.com/personalassistant) (most of my time is spent on this). It's basically an AI with access to real-time information that a) is incredible at writing naturally, and b) can operate your web browser to complete tasks for you.
=======
<!-- Add brief descriptions of the notebooks here -->

### reports

This folder will be created upon generated reports from the research tools provided.

### Scripts

This folder contains various Python scripts for various research and sub-agent tasks.

#### Maestro

[This project](https://github.com/Doriandarko/maestro) demonstrates an AI-assisted task breakdown and execution workflow using the Anthropic API. It utilizes two AI models, Opus and Haiku, to break down an objective into sub-tasks, execute each sub-task, and refine the results into a cohesive final output.

#### Ollama Researcher

[This project](https://www.binx.page/blog/research-assistant) was published to my blog. For a full breakdown, please view the provided [link](https://www.binx.page/blog/research-assistant).

## Contributing

Contributions to this repository are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).

---
>>>>>>> Stashed changes
