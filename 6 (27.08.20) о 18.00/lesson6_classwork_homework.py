##################################################

# Output maximum from n numbers. The first option.
# numbers = []
# amount_numbers = int(input("Please, enter the count of the elements of sequence: "))
# for i in range(amount_numbers):
#     n = int(input("Please enter the element: "))
#     numbers.append(n)
# max_num = numbers[0]
# min_num = numbers[0]
# for i in range(amount_numbers):
#     if numbers[i] > max_num:
#         max_num = numbers[i]
#     if numbers[i] < min_num:
#         min_num = numbers[i]
# print("Maximum number = {}. Minimum = {}.".format(max_num,min_num))

###################################################

# Output maximum from n numbers. The second option.
# user_count = int(input("Enter quantity of numbers: "))
# num_list = [int(input("Enter your next number: ")) for i in range (user_count)]
# print(num_list)
# print("Max number is:", max(num_list))
# print("Min number is:", min(num_list))

###################################################

# Output maximum from n numbers. The second option - more short.
# num_list = [int(input("Enter {} number: ".format(i+1))) for i in range(int(input("Enter quantity of sequence: ")))]
# print(num_list)
# print("Maximum number is:", max(num_list))
# print("Minimum number is:", min(num_list))

###################################################

# Output maximum from n numbers. The third option - shortest.
# amount_of_numbers = int(input("Input amout of numbers: "))
# list_of_numbers = [int(input("Input the next number: ")) for i in range(amount_of_numbers)]
# print("Maximum number = {}. Maximum number = {}.".format(max(list_of_numbers), min(list_of_numbers)))

###################################################

# This is first hometask (first part). Output even numbers from 1 to 10.
# even_numbers = []
# for i in range(11):
#     if i > 0 and i%2 == 0:
#       even_numbers.append(i)
# print("These are even numbers from 1 to 10, which are divisible by two:", even_numbers)

###################################################

# This is first hometask (second part). Output odd numbers from 1 to 10, which are divisible by 3.
# odd_numbers = []
# for i in range(11):
#     if i > 0 and i%3 == 0:
#         odd_numbers.append(i)
# print("These are odd numbers from 1 to 10, which are divisible by three:", odd_numbers)

###################################################

# This is first hometask (third part). Output numbers that are not divided by 2 and 3. 
# numbers = []
# for i in range(11):
#     if i > 0 and i%2 == 0 or i%3 == 0:
#         continue
#     else:
#         numbers.append(i)
# print("These are numbers from 1 to 10, that are not divided into two and are not divided into three:", numbers)

###################################################

# This is first hometask (all part). The first option.
# for number in range(1,11):
    # if number % 2 == 0:
    #     print(number, "is even multiple of 2")
    # elif number % 3 == 0:
    #     print(number, "is an odd multiple of 3")
    # else:
    #     print(number, "not divisible by 2 and 3")

###################################################

# This is first hometask (all part). The second option.
# group_numbers_1 = []
# group_numbers_2 = []
# group_numbers_3 = []
# for num in range(1,11):
#     if num % 2 == 0:
#         #print(num, "is an even multiple of 2")
#         group_numbers_1.append(num)
#     elif num % 3 == 0:
#         #print(num, "is an odd multiple of 3")
#         group_numbers_2.append(num)
#     else:
#         #print(num, "not divisible by 2 and 3")
#         group_numbers_3.append(num)
# print(group_numbers_1)
# print(group_numbers_2)
# print(group_numbers_3)

###################################################

# This is second hometask (the first option). Calculating the factorial of a number entered by the user.
# user_number = int(input("Enter the factorial of the number to calculate: "))
# for number in range (user_number):
#   if number > 0:
#     user_number=user_number*number
# print("The factorial of your number is equal to", user_number)

###################################################

# This is second hometask (the second option). Calculating the factorial of a number entered by the user.
# number = int(input('Enter number: '))
# list_number = list(range(1, number+1))
# factorial_value = 1
# for multiply in list_number:
#     factorial_value = factorial_value * multiply
# print(factorial_value)

###################################################

# This is second hometask (the third option). Calculating the factorial of a number entered by the user.
# num = int(input("Enter number: "))
# factorial = 1
# # chek if the number is negative, positive or zero
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers.")
# elif num == 0:
#     print("The factorial of the number 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial = factorial+*i
#     print("The factorial of {0} is {1}".format(num, factorial))

###################################################

# This is second hometask (the fourth option). Calculating the factorial of a number entered by the user.
# number = int(input("Enter a positive integer: "))
# factorial = 1
# for i in range(1,number+1):
#     factorial*=i
# print("The factorial of the number", number, "is equal to", factorial)

###################################################

# This is third hometask. Script to check user login.
# user_login = input("Enter your login: ")
# tru_login = "First"
# while tru_login != user_login:
#   user_login = input("Error: this is an incorrect login. Enter your login again: ")
# else:
#   print("Congratulations", user_login, "! You are logged in.")

###################################################

# This is third hometask (the second option). Script to check user login.
# user_name = input("Hello, please input your Log in: ")
# while user_name != "First":
#     print("Error: wrong username, please try one more time.")
#     user_name = input("Username: ")
#     # print(user_name)
# print("Greeting. Access granted!!!", user_name)