from src.problem171 import find_busiest_period


def test_find_busiest_period():
    entries = [
        {"timestamp": 1526579928, "count": 3, "type": "enter"},
        {"timestamp": 1526579982, "count": 4, "type": "enter"},
        {"timestamp": 1526580054, "count": 5, "type": "exit"},
        {"timestamp": 1526580128, "count": 1, "type": "enter"},
        {"timestamp": 1526580382, "count": 3, "type": "exit"},
    ]
    assert find_busiest_period(entries) == (1526579982, 1526580054)
