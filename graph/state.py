from typing import TypedDict, List


class UniversityState(TypedDict):
    user_query: str
    intent: str
    response: str

    history: List[str]
    user_name: str