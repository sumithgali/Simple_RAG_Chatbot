from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following question:

Here is the conversatoin history: {Context}

Question: {Question}

Answer:
"""

model = OllamaLLM(model = "llama3")

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def handle_conversation():
    context =""
    print("Welcome to AI Chatbot: Type 'Exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"Context": context, "Question": user_input})
        print(f"AI: {result}")
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()