from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph, END, START
from typing import TypedDict

# connect to local ollama model
llm = OllamaLLM(model="phi3")

# function to generate response
def generate_response(question: str):
    response = llm.invoke(question)
    return response

# state structure
class ChatState(TypedDict):
    question: str
    answer: str

# LangGraph node
def chatbot_node(state: ChatState):
    question = state["question"]
    answer = generate_response(question)
    return {"answer": answer}

# build graph
builder = StateGraph(ChatState)

builder.add_node("chatbot", chatbot_node)

builder.add_edge(START, "chatbot")

builder.add_edge("chatbot", END)

chatboot = builder.compile()
