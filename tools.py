import ast
import operator
import re

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}


def calculate(expression):
    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](
                evaluate(node.left),
                evaluate(node.right)
            )

        if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](evaluate(node.operand))

        raise ValueError("Unsupported mathematical expression")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)


def analyze_text(text):
    words = text.split()
    sentences = re.split(r'[.!?]+', text.strip())

    sentences = [s for s in sentences if s.strip()]

    return {
        "word_count": len(words),
        "character_count": len(text),
        "sentence_count": len(sentences)
    }