"""
Merge Overlapping Orders
Problem

Given a list of time intervals representing food preparation windows, merge all overlapping intervals.

Input
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
Output
[(1, 6), (8, 10), (15, 18)]
"""

def merge_overlapping_orders(orders):

    new_orders = []
    new_orders.append(orders[0])

    for each_order in orders[1:]:
        if each_order[0] <= new_orders[-1][1]:
            new_orders[-1] = (min(new_orders[-1][0], each_order[0]), max(new_orders[-1][1], each_order[1]))
        else:
            new_orders.append(each_order)

    return new_orders

print(merge_overlapping_orders([(1, 3), (2, 6), (8, 10), (15, 18)]))

