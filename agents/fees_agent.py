from config import DEBUG
from graph.state import UniversityState
from utils.data_loader import load_data
from utils.ai_helper import generate_answer
from utils.retriever import retrieve_relevant_data


def fees_agent(state: UniversityState):

    if DEBUG:
        print("[Fees Agent] Executing...")

    data = load_data()

    fees = data["fees"]

    query = state["user_query"]

    context = retrieve_relevant_data(
        query=query,
        data=fees
    )

    answer = generate_answer(
    user_question=state["user_query"],
    context=context,
    history=state["history"]
)

    state["response"] = answer

    return state