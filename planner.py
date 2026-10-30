def create_plan(goal):
    goal = goal.lower()

    print("\n[PLANNER] Creating execution plan...")

    if any(word in goal for word in ["calculate", "multiply", "add", "divide"]):
        return [
            "Understand the calculation request",
            "Execute the calculator tool",
            "Review the calculation result"
        ]

    elif any(word in goal for word in ["analyze", "analyse", "text", "words"]):
        return [
            "Understand the text analysis request",
            "Execute the text analyzer tool",
            "Review the analysis result"
        ]

    else:
        return [
            "Understand the user's objective",
            "Identify available tools",
            "Report that the task needs a supported tool"
        ]