import subprocess
import time
import datetime
import platform
import os
import glob
import pyautogui
import pygetwindow as gw
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

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

# 2. Date and Time Tool
@tool
def get_date_time() -> str:
    """Retrieves the current date and time."""
    now = datetime.datetime.now()
    return now.strftime("Current Date and Time: %Y-%m-%d %H:%M:%S")

# 3. Notepad Tool
@tool
def open_notepad_and_write(text: str) -> str:
    """Opens Windows Notepad and writes user-provided text."""
    print(f"\n[EXECUTING] Opening Notepad...")
    try:
        subprocess.Popen("notepad.exe")
        time.sleep(1.5)
        notepad_windows = gw.getWindowsWithTitle("Notepad")
        if notepad_windows:
            notepad_windows[0].activate()
            time.sleep(0.5)
        pyautogui.write(text, interval=0.05)
        return f"Opened Notepad and wrote: '{text}'"
    except Exception as e:
        return f"Failed to automate Notepad: {str(e)}"

# 4. File Search Tool
@tool
def search_files(directory: str, extension: str) -> str:
    """Searches for files by extension in a specified directory."""
    print(f"\n[EXECUTING] Searching for {extension} files in {directory}...")
    try:
        search_path = os.path.join(directory, f"**/*.{extension}")
        files = glob.glob(search_path, recursive=True)
        if files:
            return f"Found files: {files[:10]}" # Return up to 10 files
        return f"No .{extension} files found in {directory}."
    except Exception as e:
        return f"Error searching files: {str(e)}"

# 5. File Creation Tool
@tool
def create_text_file(filepath: str, content: str) -> str:
    """Creates a text file with user-provided content at the specified path."""
    print(f"\n[EXECUTING] Creating file at {filepath}...")
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully created file at {filepath} with content: '{content}'"
    except Exception as e:
        return f"Failed to create file: {str(e)}"

# 6. System Information Tool
@tool
def get_system_info() -> str:
    """Retrieves operating system, processor, and memory information."""
    uname = platform.uname()
    return (f"OS: {uname.system} {uname.release} (Version: {uname.version})\n"
            f"Node Name: {uname.node}\n"
            f"Processor: {uname.processor}")

# Initialize LLM & Bind Tools
llm = ChatOllama(model="llama3.2:3b", temperature=0)
tools = [
    open_calculator, 
    get_date_time, 
    open_notepad_and_write, 
    search_files, 
    create_text_file, 
    get_system_info
]
llm_with_tools = llm.bind_tools(tools)

tool_map = {
    "open_calculator": open_calculator,
    "get_date_time": get_date_time,
    "open_notepad_and_write": open_notepad_and_write,
    "search_files": search_files,
    "create_text_file": create_text_file,
    "get_system_info": get_system_info
}

# Agent Execution Loop
def run_agent():
    system_prompt = (
        "You are a helpful AI assistant with access to multiple tools including calculator, "
        "date/time, notepad automation, file search, file creation, and system information. "
        "Always select the appropriate tool based on the user's request."
    )
    
    print("Multi-Tool AI Agent Ready! Type 'exit' to quit.\n")
    
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
            print(f"Agent: {final_response.content}\n")
        else:
            print(f"\nAgent: {ai_msg.content}\n")

if __name__ == "__main__":
    run_agent()