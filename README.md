# Multi-LLM-Judge-Aggregator

---

## Overview

**Multi-LLM-Judge-Aggregator** is an advanced Python project that enhances multi-model AI interaction.  
Unlike basic aggregators that only display outputs from multiple models, this system employs a third **judge model** to analyze, compare, and synthesize responses into one optimized answer.

---

## Key Idea

Most multi-LLM tools merely collect responses.  
This project introduces an intelligent layer: after collecting answers from multiple models, a dedicated **judge model** evaluates them and generates a high-quality synthesized response that combines the strongest elements of each.

---

## Key Features

- **Intelligent Response Analysis** – a judge model evaluates and compares different LLM outputs.  
- **Response Synthesis** – produces one optimized answer using reasoning and evaluation.  
- **Multi-Model Support** – integrates with various LLMs via the OpenRouter API.  
- **LangChain Framework** – built with modern, modular LLM workflow tools.  
- **Performance Tracking** – measures response time for each model.  
- **Error Handling** – includes robust handling for network or API issues.

---

## Technologies Used

- Python 3.9+  
- LangChain  
- langchain-openai  
- langchain-core  
- python-dotenv  
- OpenRouter API

---

## Project Structure
Multi-LLM-Judge-Aggregator/
│── main.py # Main application entry point
│── .env # API configuration (excluded from repo)
│── requirements.txt # Dependencies
│── README.md # Documentation

---

## How It Works

1. The user enters a question.  
2. The system sends the prompt to two different LLMs simultaneously.  
3. Both models return their answers.  
4. A third **judge model** receives both answers and the original question.  
5. The judge analyzes, compares, and synthesizes them into a single, improved answer.  
6. The optimized response is returned to the user.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MykhailoTymoshenko08/Multi-LLM-Judge-Aggregator.git
cd Multi-LLM-Judge-Aggregator
```

### 2. Install dependencies
```bash
pip install langchain-openai langchain-core python-dotenv
```

### 3. Set up your API key
1) Obtain an API key from OpenRouter
2) Create a .env file in the project root.
3) Add your key as follows:
```bash
API_KEY=your_key_here
```

## Usage

###Run the application:
```bash
python app.py
```
When prompted, enter your question, for example:
```bash
Enter your request: What is machine learning?
```

## Example Output
```bash
Original answers:
Model 1: Machine learning is a subset of AI...
Model 2: ML involves algorithms that improve through experience...

Final answer:
Based on analysis: Machine learning is an AI subset where algorithms learn from data and improve their performance over time.
```

## Default Model Configuration
###Role	                 Model	                                   Source
Answer Generator 1	   meta-llama/llama-3.3-70b-instruct:free	   OpenRouter
Answer Generator 2	   google/gemma-3-27b-it:free	               OpenRouter
Judge Model	           mistralai/devstral-2512:free	             OpenRouter

You can modify these defaults in app.py.

##Project Evolution

This project represents the third generation of LLM aggregation systems:
1. Multi-LLM-Requests_Type – basic version using raw HTTP requests.
2. Multi-LLM-LangChain_Type – intermediate version leveraging LangChain.
3. Multi-LLM-Judge-Aggregator – current version with analytical synthesis.

