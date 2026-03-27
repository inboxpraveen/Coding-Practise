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
    if not orders:
        return []
    
    orders.sort()
    merged = [orders[0]]

    for start, end in orders[1:]:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    return merged

print(merge_overlapping_orders([(1, 3), (2, 6), (8, 10), (15, 18)]))

