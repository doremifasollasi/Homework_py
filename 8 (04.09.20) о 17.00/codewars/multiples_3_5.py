# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Note: If the number is a multiple of both 3 and 5, only count it once. 
# Also, if a number is negative, return 0(for languages that do have them)

def solution(number):
    numbers_list = []
    for num in range(number):
        numbers_list = []
        if num <= 0:
            numbers_list.append(0)
        elif num%5 == 0:
            numbers_list.append(num)
        elif num%3 == 0:
            numbers_list.append(num)
        else:
            numbers_list = numbers_list
    return sum(numbers_list)
        
#########################################

# def solution(number):
#     total = 0
#     for num in range(number):
#         if num % 3 == 0 or num % 5 == 0:
#             total += num
#     return total

########################################

def solution(number):
    return sum(x for x in range(number) if x%3 == 0 or x%5 == 0)