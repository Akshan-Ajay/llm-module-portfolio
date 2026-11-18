import subprocess
import time
import pyautogui
import pygetwindow as gw
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

# 1. Define the Calculator Tool
@tool
def open_calculator(expression: str) -> str:
    """Opens Windows Calculator and enters a mathematical expression to calculate."""
    print(f"\n[EXECUTING] Opening Windows Calculator...")
    try:
        subprocess.Popen("calc.exe")
        time.sleep(1.5)  # Wait for window to load

        calc_windows = gw.getWindowsWithTitle("Calculator")
        if calc_windows:
            calc_windows[0].activate()
            time.sleep(0.5)

        pyautogui.press("esc")
        pyautogui.write(expression, interval=0.1)
        pyautogui.press("enter")
        
        print(f"[SUCCESS] Expression entered into Calculator.")
        return f"Entered {expression} into Windows Calculator."
    except Exception as e:
        return f"Failed to automate calculator: {str(e)}"

# 2. Initialize LLM & Bind Tool
llm = ChatOllama(model="llama3.2:3b", temperature=0)
tools = [open_calculator]
llm_with_tools = llm.bind_tools(tools)

tool_map = {"open_calculator": open_calculator}

# 3. Agent Execution Loop
def run_agent():
    system_prompt = (
        "You are a helpful AI assistant with access to tools. "
        "When the user asks you to calculate anything, you MUST call the open_calculator tool. "
        "Never calculate the answer yourself. Pass the complete mathematical expression to the tool."
    )
    
    print("Calculator Agent Ready! Type 'exit' to quit.\n")
    
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
                print(f"[TOOL RESULT] {tool_result}\n")
                
                messages.append(
                    ToolMessage(content=str(tool_result), tool_call_id=tool_call["id"])
                )
            
            final_response = llm_with_tools.invoke(messages)
            print(f"Agent: {final_response.content}\n")
        else:
            print(f"\nAgent: {ai_msg.content}\n")

if __name__ == "__main__":
    run_agent()