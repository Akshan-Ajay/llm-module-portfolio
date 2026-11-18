import sqlite3
import subprocess
import time
import pyautogui
import pygetwindow as gw
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

# --- Database Setup for Memory ---
DB_NAME = "student_memory.db"

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

# 2. Memory Search Tool (Expanded to search all records if asking for name/identity)
@tool
def search_student_memory(query: str) -> str:
    """Retrieves previously stored user information from SQLite database based on a query."""
    print(f"\n[MEMORY] Searching database for: '{query}'")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # If asking about name, fetch all saved user interactions to give full context
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

def save_memory(query: str, response: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO memories (query, response) VALUES (?, ?)", (query, response))
    conn.commit()
    conn.close()

# Initialize LLM & Bind Tools
llm = ChatOllama(model="llama3.2:3b", temperature=0)
tools = [open_calculator, search_student_memory]
llm_with_tools = llm.bind_tools(tools)

tool_map = {
    "open_calculator": open_calculator,
    "search_student_memory": search_student_memory
}

# Agent Execution Loop with Memory
def run_agent():
    print("=========================================")
    print("INTELLIGENT STUDENT AI AGENT")
    print("SHORT-TERM MEMORY")
    print("LONG-TERM SQLITE MEMORY")
    print("WORKING MEMORY")
    print("=========================================\n")
    
    system_prompt = (
        "You are an intelligent student AI assistant with access to a calculator tool and a long-term SQLite memory search tool. "
        "When a user asks about their identity, name, or past statements, you MUST call the search_student_memory tool."
    )
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        print("\n[MEMORY] Checking for relevant context...")
        
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
                print(f"[TOOL RESULT] {tool_result}\n")
                
                messages.append(
                    ToolMessage(content=str(tool_result), tool_call_id=tool_call["id"])
                )
            
            final_response = llm_with_tools.invoke(messages)
            response_content = final_response.content
        else:
            response_content = ai_msg.content

        print(f"[SHORT-TERM MEMORY] Conversation updated.")
        print(f"\nAgent: {response_content}\n")
        
        # Save interaction to long-term memory if user introduces themselves
        if any(keyword in user_input.lower() for keyword in ["my name is", "i'm", "i am", "im "]):
            save_memory(user_input, response_content)
            print(f"[SAVED] Stored new information to SQLite memory.\n")

if __name__ == "__main__":
    run_agent()