import json

from utils.llm import llm


def generate_answer(
    user_question: str,
    context: dict,
    history: list
):

    conversation = "\n".join(history)

    prompt = f"""
You are an AI University Assistant.

Answer the student's question using ONLY the university information provided.

Previous Conversation:
{conversation}

University Information:
{json.dumps(context, indent=2)}

Current Student Question:
{user_question}

Instructions:

- Use the previous conversation to understand follow-up questions.
- If the student asks "yes", "tell me more", "what about that", "can I", etc., infer what they are referring to.
- Do not invent information.
- If the answer is unavailable in the university information, clearly say so.
- Answer naturally and professionally.
"""

    response = llm.invoke(prompt)

    return response.content