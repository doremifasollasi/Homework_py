# The first task of classwork. 

# def arithmetic_mean():
#     """
#     This function calculates the arithmetic mean of two numbers. 
#     These numbers are arguments that must be specified.
#     """
#     quantity = int(input("Enter the quantity of numbers: "))
#     list_numbers = []
#     for user_numbers in range(quantity):
#         user_numbers = int(input("Enter the next number: "))
#         list_numbers.append(user_numbers)
    
#     total = sum(list_numbers)
        
#     return total / quantity

# print(arithmetic_mean())

#############################

# def avg_num (*args):
#     """This function counts avg value for few numbers"""
#     final_avg_result = 0
#     for avg_result in args:
#         final_avg_result += avg_result
#     return final_avg_result / len(args)

# print(avg_num(100,5,1,1))

#############################

# def aver_arif(*args):
#     sum_numbers = 0
#     for num in args:
#         sum_numbers += num
#     return sum_numbers / (len(args))

#############################

# def ser_arifmetichne(*args):
#     return sum(args)/len(args)

#################################
#################################

# The second task of classwork. 

# def largest_number(first_number, second_number):
#     """
#     This function determines the maximum number of two numbers. 
#     In order for it to work, you need to call the function 
#     and in parentheses be sure to enter two numbers, separated by a comma.
#     """
#     if first_number > second_number:
#         return first_number
#     else:
#         return second_number

# print("Max number is", largest_number(100,22))   
     
####################

# def max_num (num1,num2):
#     """
#     This function determines the maximum number of two numbers. 
#     In order for it to work, you need to call the function 
#     and in parentheses be sure to enter two numbers, separated by a comma.
#     """    
#     max_number = None
#     if num1-num2 >= 0:
#         max_number = num1
#     else:
#         max_number = num2

#     return max_number

# print(max_num(155,55))

####################

# def max_number(*arg):
#     return max(arg)

####################

# def max_chyslo(a,b):
#     return max(a,b)

####################

# def max_num(first, second):
#     if first >= second:
#         return first
#     else:
#         return second

####################

# def max(num1,num2):
#     """Function enter 2 variable"""
#     return num1 if num1 > num2 else num2

####################

# def maximum_number(x, y):
# 	if x>y:
# 		return (x)
# 	else:
# 		return (y)
# print(max(5, 6))

#################################
#################################

# The third task of classwork (homework)

def area_triangle(user_choice):
    """
    This function calculates the area of a triangle,
    using the dimensions of all sides of the triangle that the user enters.
    """
    from math import sqrt
    a = float(input("Specify the dimensions of one side of the triangle: "))
    b = float(input("Now the second side: "))
    c = float(input("And the last - the third side of the triangle: "))   
    p = (a+b+c)/2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return f"The area of the triangle is equal to {s}"

    ###################################

    # import math
    # s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    # return f"The area of the triangle is equal to {s}"
 
    ###################################
    
    # a = float(input("Input basis: "))
    # h = float(input("Input height: "))
    # return "Area = {}".forman(0.5 * a *h)

def area_rectangle(user_choice):
    """
    This function calculates the area of a rectangle,
    using the dimensions of all sides of the rectangle that the user enters.
    """
    a = float(input("Specify the dimensions of one side of the triangle: "))
    b = float(input("Now the second side: "))
    s = a*b
    return "The area of the rectangle is equal to " + str(s)
    
    ############################

    # return "Square = {}".format(s)

def area_circle(user_choice):
    """
    This function calculates the area of a circle,
    using the dimensions of all sides of the circle that the user enters.
    """
    import math
    r = float(input("Enter the radius of the circle: "))       
    s = math.pi * (r**2)
    return "The area of the circle is equal to {}".format(s)

    #####################################

    # PI = 3.14
    # r = float(input("Input radius: "))
    # return ("Square = {}".format(PI * r ** 2))



user_choice = int(input('''
    If you need to calculate the area of a triangle, enter the number 1, 
    if the rectangle - 2, if the circle - 3. Enter the appropriate number: '''))

while user_choice not in (1,2,3):
    user_choice = int(input('''
    You have not entered any of the suggested numbers. 
    Enter the appropriate number (1 or 2 or 3): 
    '''))
else:
    if user_choice == 1:
        print (area_triangle(user_choice))
    elif user_choice == 2:
        print (area_rectangle(user_choice))
    else: 
        print (area_circle(user_choice))

##############################################

# user_choice = input("1 - rectangle, 2 - triangle, 3 - circle: ")
# if user_choice == "1":
#     print(area_rectangle(user_choice))
# elif user_choice == "2":
#     print(area_triangle(user_choice))
# elif user_choice == "3":
#     print(area_circle(user_choice))
# else:
#     print("Input error")


#################################################
#################################################


# The third task of classwork (homework), second option is less clear.

figure = input("1 - rectangle, 2 - triangle, 3 - circle: ")
PI = 3.14
if figure == "1":
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    print("Area = {}".format(a*b))
elif figure == "2":
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    area = 0,5*a*h
    print("Area = {}".format(area))
elif figure == "3":
    r = float(input("Input radius: "))
    print("Area = {}".format(PI*r**2))
else:
    print("Input error")

#################################################
#################################################


# The fourth task of classwork (homework)

def count_symbols(word):
    """Counting symbols in the string"""
    result = {}
    for x in word:
        if x in result:
            continue
        else:
            result.update({str(x): word.count(x)})
    return result
print(count_symbols)
print(count_symbols)
print(count_symbols)

#########################################


def count_symbols_2(string):
    """Counting symbols in the string"""
    my_tuple_full = tuple(''.join(string.split()))
    my_dict = {symbol: my_tuple_full.count(symbol) for symbol in my_tuple_full}
    return my_dict
print(count_symbols("House home"))

#################################################
#################################################

# The fifth task of classwork (homework)

# Such a technique (calling a function of itself) is called recursion, 
# and the function itself is called recursive.

def factorial(number_user):
    """Functions for calculating the factorial of a number entered by the user"""
    if number_user == 0:
        return 1
    else:
        return number_user * factorial(number_user - 1)

print(factorial(5))