from config import DEBUG
from graph.state import UniversityState


def unknown_agent(state: UniversityState):
    if DEBUG:
      print("[Unknown Agent] Executing...")
    state["response"] = (
        "Sorry, I can only answer questions related to:\n\n"
        "• Admissions\n"
        "• Examinations\n"
        "• Fees\n"
        "• Scholarships\n\n"
        "Please ask a question about one of these topics."
    )

    return state