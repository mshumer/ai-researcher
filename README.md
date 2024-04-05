# ai-researcher
[![Twitter Follow](https://img.shields.io/twitter/follow/mattshumer_?style=social)](https://twitter.com/mattshumer_) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fn2Xisstp0d30_bAaLPA1y-0_svojLF3?usp=sharing)

The AI Researcher is an AI agent that utilizes Claude 3 and SERPAPI to perform comprehensive research on a given topic. It breaks down the research process into subtopics, generates individual reports for each subtopic, and then combines them into a final comprehensive report.

## Features

- Generates a detailed checklist of subtopics to research for a given topic
- Performs multiple rounds of searches and analysis for each subtopic
- Generates individual reports for each subtopic
- Incorporates feedback from a "boss" persona to identify missing information and improve the reports
- Combines the subtopic reports into a comprehensive final report

## Usage

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
