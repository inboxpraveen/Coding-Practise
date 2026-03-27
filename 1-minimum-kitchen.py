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

    kitchens = []
    kitchen_counter = 0

    for order in orders:
        allocated = False
        for kitchen in kitchens:
            if order[0] >= kitchen[1]:
                allocated = True
                break

        if not allocated:
            kitchen_counter += 1
            kitchens.append(order)
    
    return kitchen_counter


print(minimum_kitchens_required([(9, 12), (10, 11), (11, 13), (12, 14)]))
