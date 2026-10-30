from tools import calculate, analyze_text


def execute_tool(goal, user_input=""):
    goal = goal.lower()

    print("\n[EXECUTOR] Executing selected tools...")

    if any(word in goal for word in ["calculate", "multiply", "add", "divide"]):
        expression = input("Enter mathematical expression: ")

        try:
            result = calculate(expression)
            return {"tool": "Calculator", "result": result}
        except Exception as error:
            return {"tool": "Calculator", "error": str(error)}

    elif any(word in goal for word in ["analyze", "analyse", "text", "words"]):
        text = input("Enter the text to analyze: ")
        return {
            "tool": "Text Analyzer",
            "result": analyze_text(text)
        }

    return {"error": "No supported tool found"}