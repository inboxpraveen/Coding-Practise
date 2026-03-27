"""
Insert New Order Slot
Problem

You are given a list of non-overlapping, sorted intervals. Insert a new interval and merge if necessary.

Input
intervals = [(1, 3), (6, 9)]
new_interval = (2, 5)
Output
[(1, 5), (6, 9)]
"""

def insert_order_slot(intervals, new_interval):
    res = []
    i = 0

    # before overlap
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    # merge
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval = (
            min(new_interval[0], intervals[i][0]),
            max(new_interval[1], intervals[i][1])
        )
        i += 1

    res.append(new_interval)

    # after overlap
    while i < len(intervals):
        res.append(intervals[i])
        i += 1

    return res


print(insert_order_slot([(1, 3), (6, 9)], (2, 5)))

