from src.problem163 import evaluate_reverse_polish_expression


def test_evaluate_expressions():
    tests = [
        {"expression": [5, 3, "+"], "expected": 8},
        {"expression": [15, 7, 1, 1, "+", "-", "/", 3,
                        "*", 2, 1, 1, "+", "+", "-"], "expected": 5}
    ]

    for test in tests:
        expression, expected = test["expression"], test["expected"]
        assert evaluate_reverse_polish_expression(expression) == expected
