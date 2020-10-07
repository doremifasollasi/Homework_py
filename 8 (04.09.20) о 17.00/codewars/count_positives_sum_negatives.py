# Given an array of integers. 
# Return an array, where the first element is the count of positives numbers 
# and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.

def count_positives_sum_negatives(arr):
    count = 0
    total = 0
    if not arr:
            return []
    for num in arr:
        if num > 0:
            count+=1
        elif num < 0:
            total+=num
    return [count,total]

# ################

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []