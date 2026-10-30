from planner import create_plan
from executor import execute_tool


def run_agent():

    print("=" * 45)
    print("       MULTI-STEP AI AGENT")
    print("=" * 45)

    goal = input("\nWhat task should I perform? ")

    # Step 1: Planning
    plan = create_plan(goal)

    print("\n--- EXECUTION PLAN ---")

    for number, step in enumerate(plan, start=1):
        print(f"{number}. {step}")

    # Step 2: Execution
    result = execute_tool(goal)

    print("\n--- EXECUTION RESULT ---")
    print(result)

    # Step 3: Review
    print("\n--- AGENT REVIEW ---")

    if "error" not in result:
        print("Task completed successfully!")
    else:
        print("Task could not be completed.")

    print("\nAgent execution finished.")


if __name__ == "__main__":
    run_agent()