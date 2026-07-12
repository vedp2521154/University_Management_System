from config import DEBUG
from graph.state import UniversityState


def response_agent(state: UniversityState):

    if DEBUG:
        print("[Response Agent] Formatting response...")

    response = state["response"].strip()

    state["response"] = response

    return state