from typing import List, TypedDict

class GraphState(TypedDict):
    """
    Represents the state of the graph

    Attributes:
        question: question
        generation: LLM Generation
        web_search: Whether to search online
        documents: List of documents
    """
    question: str
    generation: str
    web_search: bool
    documents: List[str]