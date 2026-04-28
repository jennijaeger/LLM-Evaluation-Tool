# LLM Evaluation Tool

A practical benchmarking tool for evaluating and comparing Large Language Models (LLMs) such as GPT, Claude, and Gemini using structured prompt scenarios.

This project was developed to analyze model behavior across realistic tasks such as reasoning, code generation, and structured outputs.

---

# Project Overview

This tool provides a structured framework to benchmark multiple LLMs across different categories.

Each model response is automatically evaluated using scoring rules and performance metrics such as latency and response quality.

The goal of this project is to create a reproducible evaluation workflow that allows objective comparison between models.

---

# Supported Models

Currently integrated:

- GPT (OpenAI)
- Claude (Anthropic)
- Gemini (Google)

The system is modular and allows adding additional models easily.

---

# Features

- Multi-model evaluation framework
- Scenario-based testing using JSON
- Automatic response scoring
- Latency measurement
- CSV result storage
- Result analytics using Pandas
- Interactive visualization dashboard (Streamlit)
- Modular architecture for extensibility

---

# Evaluation Categories

The benchmark includes realistic prompt categories:

- Code Generation
- Bug Fixing
- JSON Output Generation
- Summarization
- Logical Reasoning

Each category tests different capabilities of language models.

---

# Project Structure

```
LLM-Evaluation-Tool/
│
├── app.py
│   Streamlit dashboard for visualization
│
├── run_evaluation.py
│   Main script to execute benchmark scenarios
│
├── run_single_prompt.py
│   Runs a single prompt across models
│
├── analyze_results.py
│   Generates statistical model comparisons
│
├── llm_clients.py
│   Contains API clients for all models
│
├── scenarios.json
│   Benchmark scenarios definition
│
├── test_llm_connection.py
│   Tests API connectivity
│
├── results/
│   Stores generated evaluation results
│
├── .env
│   API keys (not included in repository)
│
├── .gitignore
│
└── README.md
```
---
# Installation
Clone the repository:

```bash
git clone https://github.com/jenni002/LLM-Evaluation-Tool.gitcd LLM-Evaluation-Tool
```
Install dependencies:
```
pip install -r requirements.txt
```
Create a .env file:
```
OPENAI_API_KEY=your_openai_keyANTHROPIC_API_KEY=your_anthropic_keyGEMINI_API_KEY=your_gemini_key
```

---

# Running the Evaluation
Execute benchmark scenarios:
```
python run_evaluation.py
```
The results will be stored automatically in:
```
results/evaluation_timestamp.csv
```
---

# Running the Dashboard
Start the Streamlit dashboard:
```
streamlit run app.py
```
This dashboard visualizes:
- Average score per model
- Latency comparison
- Score per category
- Detailed model outputs
  
---

# Example Metrics Collected
The system automatically calculates:
- Structure Score
- Content Score
- Length Score
- Total Score
- Response Latency
These metrics allow direct comparison between models.

--- 

# Technologies Used
This project uses:
- Python
- OpenAI API
- Anthropic API
- Google Gemini API
- Pandas
- Streamlit
- JSON
- Git
- Environment Variables (.env)

---

# Use Cases
This tool can be used for:
- LLM benchmarking
- Prompt engineering evaluation
- Model comparison
- AI system testing
- Research experiments
- Performance monitoring

---

# Future Improvements
Planned enhancements:
- Advanced scoring algorithms
- Visualization improvements
- Additional model integrations
- Automated report generation
- Support for multimodal models

---

# Author
Jenny Jäger

This project was developed as part of a practical AI engineering portfolio focused on evaluating and comparing large language models in real-world scenarios.

