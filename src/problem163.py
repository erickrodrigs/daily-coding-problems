"""
This problem was asked by Jane Street. (HARD)

Given an arithmetic expression in Reverse Polish Notation,
write a program to evaluate it.

The expression is given as a list of numbers and operands.
For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
should return 5, since it is equivalent to
((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""


def evaluate_reverse_polish_expression(expression):
    def calculate_value(a, b, operand):
        return {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b,
        }[operand]

    stack = []
    operators = {'+', '-', '*', '/'}

    for item in expression:
        if item in operators:
            number_b = stack.pop()
            number_a = stack.pop()
            value = calculate_value(number_a, number_b, item)
            stack.append(value)
        else:
            stack.append(item)

    return stack.pop()


"""
SOLUTION:
- time: O(n)
- space: O(n)
"""
