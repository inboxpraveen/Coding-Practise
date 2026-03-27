"""
Minimum Kitchens Required (Meeting Rooms Variant)
Problem

You are given a list of food preparation orders. Each order has a start time and end time during which a kitchen is occupied.

Return the minimum number of kitchens required to process all orders without conflict.

Input
orders = [(9, 12), (10, 11), (11, 13), (12, 14)]
Output
2
Constraints
1 ≤ n ≤ 10⁴
0 ≤ start < end ≤ 10⁹
"""

def minimum_kitchens_required(orders):
    orders.sort()
    kitchens = []

    for start, end in orders:
        allocated = False
        for i in range(len(kitchens)):
            if start >= kitchens[i]:
                kitchens[i] = end
                allocated = True
                break
        
        if not allocated:
            kitchens.append(end)
    
    return len(kitchens)


print(minimum_kitchens_required([(9, 12), (10, 11), (11, 13), (12, 14)]))
