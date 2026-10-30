# 🤖 Multi-Step AI Agent Using Python

A beginner-friendly multi-step AI agent built using Python. This project demonstrates how an intelligent agent can understand a user's task, create an execution plan, select appropriate tools, execute operations, and review the results.

## 📌 Project Overview

The Multi-Step AI Agent follows a structured workflow to perform tasks through multiple stages.

Instead of executing a task in a single step, the agent breaks it down into smaller operations and processes them systematically.

The current implementation uses rule-based task planning and tool selection.

## 🎯 Project Objectives

- Understand multi-step agent architecture.
- Implement task planning and execution.
- Develop reusable Python tools.
- Perform mathematical calculations.
- Analyze text and generate statistics.
- Understand how AI agents coordinate different components.

## ⚙️ Technologies Used

- Python 3
- Python Standard Library
- Abstract Syntax Trees (AST)
- Regular Expressions
- Git and GitHub
- Visual Studio Code

## ✨ Key Features

**1. Task Planning**
- Understands the user's objective.
- Breaks tasks into smaller steps.
- Generates an execution plan.

**2. Tool Execution**
- Selects tools based on the user's request.
- Executes mathematical calculations.
- Performs text analysis.

**3. Calculator Tool**
- Addition
- Subtraction
- Multiplication
- Division
- Exponentiation

**4. Text Analyzer**
- Counts words.
- Counts characters.
- Counts sentences.

**5. Result Review**
- Checks whether execution returned an error.
- Reports the execution status.

## 🏗️ Project Architecture

```text
Multi-Step-AI-Agent/
│
├── agent.py
├── planner.py
├── executor.py
├── tools.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Descriptions

| File | Description |
|---|---|
| agent.py | Main agent execution controller |
| planner.py | Creates task execution plans |
| executor.py | Selects and executes tools |
| tools.py | Contains calculator and text analysis functions |
| requirements.txt | Project dependencies |
| README.md | Project documentation |

## 🔄 How It Works

The agent follows four main stages:

1. **User Input:** Receives a task from the user.
2. **Planning:** Creates a sequence of execution steps.
3. **Execution:** Selects and executes the appropriate tool.
4. **Review:** Displays the result and execution status.

## 💻 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Ameenkhalander/Multi-Step-AI-Agent.git
```

### Step 2: Navigate to the Project

```bash
cd Multi-Step-AI-Agent
```

### Step 3: Run the Application

Make sure Python 3 is installed.

```bash
python agent.py
```

No external Python packages are required for the current version.

## 🧪 Sample Test Cases

### Test Case 1: Calculator

**Input:**
```text
Calculate something
```

**Expression:**
```text
25 * 10 + 50
```

**Expected Output:**
```text
{'tool': 'Calculator', 'result': 300}
```

### Test Case 2: Text Analyzer
