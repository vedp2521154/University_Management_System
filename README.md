# University Management System using LangGraph

## Overview

This project is an AI-powered University Management Assistant built using LangGraph and Groq LLM. It routes user queries to specialized agents based on intent.

---

## Features

- AI Intent Classification
- Multi-Agent Architecture
- LangGraph Workflow
- Groq LLM Integration
- JSON-based Knowledge Base
- Response Formatting
- Unknown Query Handling

---

## Technologies Used

- Python
- LangGraph
- LangChain
- Groq API
- Llama 3.3
- python-dotenv

---

## Project Structure

```text
University_Management_System/
│
├── agents/
├── graph/
├── utils/
├── data/
├── app.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Sample Questions

- How do I enroll in the university?
- Tell me about fees.
- When are the semester exams?
- Scholarship details.