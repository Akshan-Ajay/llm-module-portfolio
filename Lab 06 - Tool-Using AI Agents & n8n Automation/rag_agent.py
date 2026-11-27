import sqlite3
import subprocess
import time
import os
import pyautogui
import pygetwindow as gw
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# --- Configuration & Paths ---
DB_NAME = "student_memory.db"
DATA_DIR = r"D:\MSC AI\Lab_06\data"
CHROMA_DIR = r"D:\MSC AI\Lab_06\chroma_db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            response TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Initialize or load vector store from local data folder
def get_vectorstore():
    embeddings = OllamaEmbeddings(model="qwen3-embedding:0.6b")
    
    # If vector store already exists, load it
    if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR):
        return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    
    # Otherwise, ingest PDFs from the data folder automatically
    print("\n[RAG] Building vector store from local data folder...")
    docs = []
    if os.path.exists(DATA_DIR):
        for file in os.listdir(DATA_DIR):
            if file.endswith(".pdf"):
                pdf_path = os.path.join(DATA_DIR, file)
                loader = PyPDFLoader(pdf_path)
                docs.extend(loader.load())
    
    if docs:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        splits = text_splitter.split_documents(docs)
        vectorstore = Chroma.from_documents(splits, embeddings, persist_directory=CHROMA_DIR)
        return vectorstore
    return None

# 1. Calculator Tool
@tool
def open_calculator(expression: str) -> str:
    """Opens Windows Calculator and enters a mathematical expression to calculate."""
    print(f"\n[EXECUTING] Opening Windows Calculator...")
    try:
        subprocess.Popen("calc.exe")
        time.sleep(1.5)
        calc_windows = gw.getWindowsWithTitle("Calculator")
        if calc_windows:
            calc_windows[0].activate()
            time.sleep(0.5)
        pyautogui.press("esc")
        pyautogui.write(expression, interval=0.1)
        pyautogui.press("enter")
        return f"Entered {expression} into Windows Calculator."
    except Exception as e:
        return f"Failed to automate calculator: {str(e)}"

# 2. Memory Search Tool
@tool
def search_student_memory(query: str) -> str:
    """Retrieves previously stored user information from SQLite database based on a query."""
    print(f"\n[MEMORY] Searching database for: '{query}'")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if "name" in query.lower() or "who" in query.lower():
        cursor.execute("SELECT query, response FROM memories")
    else:
        cursor.execute("SELECT query, response FROM memories WHERE query LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()
    
    if results:
        memories_str = "\n".join([f"User Statement: {r[0]} | Response: {r[1]}" for r in results])
        return f"Found stored user memories:\n{memories_str}"
    return "No matching memories found."

# 3. RAG Search Tool
@tool
def search_university_knowledge(query: str) -> str:
    """Retrieves relevant information from the university knowledge base vector store."""
    print(f"\n[EXECUTING] Searching university knowledge for: '{query}'...")
    try:
        vectorstore = get_vectorstore()
        if not vectorstore:
            return "No documents found in the data folder to search."
            
        docs = vectorstore.similarity_search(query, k=2)
        if docs:
            results = []
            for doc in docs:
                source = doc.metadata.get("source", "data\handbook.pdf")
                page = doc.metadata.get("page", 1)
                results.append(f"Source: {source}, Page: {page}\n{doc.page_content}")
            return "\n---\n".join(results)
        return "No relevant university information found in knowledge base."
    except Exception as e:
        return f"RAG Search failed: {str(e)}"

def save_memory(query: str, response: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO memories (query, response) VALUES (?, ?)", (query, response))
    conn.commit()
    conn.close()

# Initialize LLM & Bind Tools
llm = ChatOllama(model="llama3.2:3b", temperature=0)
tools = [open_calculator, search_student_memory, search_university_knowledge]
llm_with_tools = llm.bind_tools(tools)

tool_map = {
    "open_calculator": open_calculator,
    "search_student_memory": search_student_memory,
    "search_university_knowledge": search_university_knowledge
}

# Agent Execution Loop
def run_agent():
    print("=========================================")
    print("INTELLIGENT STUDENT AI AGENT (RAG + MEMORY)")
    print("=========================================\n")
    
    system_prompt = (
        "You are an intelligent student AI assistant with access to a calculator, student memory, "
        "and a university knowledge base RAG tool. When asked about university courses, degree programs, "
        "handbooks, or institutional policies, you MUST use the search_university_knowledge tool."
    )
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ]

        ai_msg = llm_with_tools.invoke(messages)
        messages.append(ai_msg)

        if ai_msg.tool_calls:
            for tool_call in ai_msg.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                
                print(f"\n[TOOL SELECTED] {tool_name}")
                print(f"[TOOL ARGUMENTS] {tool_args}")
                
                selected_tool = tool_map[tool_name]
                tool_result = selected_tool.invoke(tool_args)
                print(f"[TOOL RESULT]\n{tool_result}\n")
                
                messages.append(
                    ToolMessage(content=str(tool_result), tool_call_id=tool_call["id"])
                )
            
            final_response = llm_with_tools.invoke(messages)
            response_content = final_response.content
        else:
            response_content = ai_msg.content

        print(f"Agent: {response_content}\n")
        
        if any(kw in user_input.lower() for kw in ["my name is", "i'm", "i am", "im "]):
            save_memory(user_input, response_content)
            print(f"[SAVED] Stored new information to SQLite memory.\n")

if __name__ == "__main__":
    run_agent()