# 🎓 University Management Assistant using LangGraph

## Overview

This project is an AI-powered University Management Assistant built using LangGraph, LangChain, and Groq Llama 3.3. It intelligently classifies student queries and routes them to specialized AI agents such as Admission, Examination, Fees, and Scholarship agents to generate accurate responses.

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
## Setup

1. Clone the repository

git clone https://github.com/vedp2521154/University_Management_System.git

2. Create a virtual environment

python -m venv .venv

3. Activate it

Windows:
.venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Create a .env file

GROQ_API_KEY=your_api_key_here

6. Run

python app.py

## Sample Questions
- How do I enroll in the university?
- Tell me about fees.
- When are the semester exams?
- Scholarship details.
