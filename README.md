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

### reports

This folder will be created upon generated reports from the research tools provided.

### Scripts

This folder contains various Python scripts for various research and sub-agent tasks.

- Maestro
  - [This project](https://github.com/Doriandarko/maestro) demonstrates an AI-assisted task breakdown and execution workflow using the Anthropic API. It utilizes two AI models, Opus and Haiku, to break down an objective into sub-tasks, execute each sub-task, and refine the results into a cohesive final output.

- Ollama Researcher
  - [This project](https://www.binx.page/blog/research-assistant) was published to my blog. For a full breakdown, please view the provided [link](https://www.binx.page/blog/research-assistant).

## Contributing

Contributions to this repository are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).

---
>>>>>>> Stashed changes
