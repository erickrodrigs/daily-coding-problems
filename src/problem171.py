"""
This problem was asked by Amazon. (EASY)

You are given a list of data entries that represent entries and exits of
groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most
people in the building. Return it as a pair of (start, end) timestamps.
You can assume the building always starts off and ends up empty, i.e.
with 0 people inside.
"""


def find_busiest_period(data_entries):
    data_entries.sort(key=lambda x: x["timestamp"])

    current_people_in_the_building = 0
    max_people_in_the_building = 0
    start_time, end_time = 0, 0

    for data in data_entries:
        timestamp, count = data["timestamp"], data["count"]

        if data["type"] == "enter":
            current_people_in_the_building += count

            if current_people_in_the_building > max_people_in_the_building:
                max_people_in_the_building = current_people_in_the_building
                start_time = timestamp
        else:
            if current_people_in_the_building == max_people_in_the_building:
                end_time = timestamp

            current_people_in_the_building -= count

    return (start_time, end_time)


def test_find_busiest_period():
    entries = [
        {"timestamp": 1526579928, "count": 3, "type": "enter"},
        {"timestamp": 1526579982, "count": 4, "type": "enter"},
        {"timestamp": 1526580054, "count": 5, "type": "exit"},
        {"timestamp": 1526580128, "count": 1, "type": "enter"},
        {"timestamp": 1526580382, "count": 3, "type": "exit"},
    ]
    assert find_busiest_period(entries) == (1526579982, 1526580054)


"""
SOLUTION:
time: O(n lgn), where n is the total of data entries/exists
space: O(1)
"""
