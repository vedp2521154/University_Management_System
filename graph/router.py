from config import DEBUG
from graph.state import UniversityState
from utils.llm import llm


def intent_classifier(state: UniversityState):

    query = state["user_query"]
    history = "\n".join(state["history"])

    query_lower = query.lower()
    history_lower = history.lower()

    # -----------------------------
    # Rule-based routing (fast path)
    # -----------------------------

    # Application fee belongs to Admission
    if "application fee" in query_lower:
        state["intent"] = "admission"
        return state

    # If user was talking about admission and asks about "fee",
    # treat it as application fee instead of tuition fee.
    if (
        "fee" in query_lower
        and "tuition" not in query_lower
        and "hostel" not in query_lower
        and "library" not in query_lower
        and "exam" not in query_lower
        and "admission" in history_lower
    ):
        state["intent"] = "admission"
        return state

    # -----------------------------
    # LLM Router
    # -----------------------------

    prompt = f"""
You are an intelligent intent classifier for a University AI Assistant.

Your job is to classify the user's query into ONLY ONE intent.

Supported intents:

- admission
- exam
- fees
- scholarship
- unknown

Previous Conversation:
{history}

Current User Question:
{query}

Examples:

Question: How do I take admission?
Intent: admission

Question: What documents are required?
Intent: admission

Question: What is the application fee?
Intent: admission

Question: Eligibility criteria?
Intent: admission

Question: When are the semester exams?
Intent: exam

Question: Attendance requirement?
Intent: exam

Question: When is the admit card available?
Intent: exam

Question: When will results be published?
Intent: exam

Question: What is the tuition fee?
Intent: fees

Question: Hostel fee?
Intent: fees

Question: Library fee?
Intent: fees

Question: Can I pay online?
Intent: fees

Question: Scholarship details
Intent: scholarship

Question: Who can apply for scholarships?
Intent: scholarship

Question: Scholarship documents
Intent: scholarship

Question: Hello
Intent: unknown

Question: Weather today
Intent: unknown

Important Routing Rules:

- "Application fee", "registration fee", "admission fee", "application form", "eligibility", "required documents", "admission process", and "how to apply" ALWAYS belong to the admission intent.

- "Tuition fee", "hostel fee", "library fee", "exam fee", "payment", "refund", and "fee structure" ALWAYS belong to the fees intent.

- "Attendance", "semester exam", "admit card", "result", "grading", and "backlog" ALWAYS belong to the exam intent.

- "Scholarship", "financial aid", "merit scholarship", "government scholarship", and "scholarship eligibility" ALWAYS belong to the scholarship intent.

Rules:

1. Consider BOTH the previous conversation and the current question.
2. If the current question is a follow-up, infer its intent from the conversation history.
3. Return ONLY one of the supported intents.
4. Do not explain your answer.

Valid outputs:

admission
exam
fees
scholarship
unknown
"""

    response = llm.invoke(prompt)

    intent = response.content.strip().lower()

    if intent not in [
        "admission",
        "exam",
        "fees",
        "scholarship",
        "unknown",
    ]:
        intent = "unknown"

    if DEBUG:
        print(f"[Router] Intent detected: {intent}")

    state["intent"] = intent

    return state