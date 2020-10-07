# A program that prompts the user to enter an integer and 
# determines whether the number is even or odd, 
# taking into account the case of entering incorrect data. ​

# try:
#     user_number = input("Enter number: ")
#     # user_number = int(input("Enter number: "))
#     if user_number % 2 == 0:
#         print("Your number is even")
#     else: 
#         print("Your number is odd")
# except ValueError:
#     print('You did not enter an integer')
# except TypeError:
#     print('You didn`t enter an integer')

#############################

# def check_even(number):
#     try:
#         return 'odd mumber' if int(number)%2 else "even number"
#     except ValueError as v:
#         print('Error', v)
#     except TypeError as t:
#         print('Error', t)

# print(check_even(62))

###########################

# A program to calculate the divide of two numbers entered 
# by the user sequentially through a comma, to predict the case of division by zero, 
# cases of syntactic errors and cases of other exceptional situations. 
# Use the else and finally blocks.​

# def divide_two_numbers(a,b):
#     try:
#         # Якщо input, то потрібно зі str переобразити в int
#         # a = int(a)
#         # b = int(b)
#         return a/b
#     except ZeroDivisionError as e:
#         return 'Error', e
#     except SyntaxError as e:
#         return 'Error', e
#     except:
#         return 'There are errors in the code'
#     else:
#         return 'There are no errors in the code'
#     finally:
#         return 'The end'

# print(divide_two_numbers(8,4))

#######################

# try:
#     # eval перетворює зі стрінга в інтеджер та розділяє по комі на окремі зміні
#     num1, num2 = eval(input('Enter two number, separated by a comma: '))
#     result = num1 / num2
#     print('Result is', result)

#######################

# class CustomError(Exception):
#     def __init__(self, data):
#         self.data = data

#     def __str__(self):
#         return repr(self.data)

# total_score = int(input("Enter expert score: "))
# try:
#     num_of_group = int(input("Enter number of your group: "))
#     if num_of_group < 1:
#         raise CustomError("Number of your group can't be less than 1")
# except CustomError as e:
#     print("We obtain error:", e.data)

#######################

# HOMEWORK
# A program that prompts the user to enter their age, 
# and then displays a message stating whether the age is even or odd. 
# The program must provide the ability to enter a negative number, and in this case generate an exception. 
# The master code should call a function that processes the information entered. 


# class CustomError(Exception):
#     def __init__(self, data):
#         self.data = data

#     def __str__(self):
#         return repr(self.data)

# try:
#     user_age = int(input("Enter your age: "))
#     if user_age < 0:
#         raise CustomError("You enter no correct number")
#     elif user_age % 2 == 0:
#         print('Your age is even')
#     else:
#         print('Your age is odd')
        
# except CustomError as e:
#     print("We obtain error:", e.data)


#######################

# HOMEWORK
# Write a program that analyzes the entered number and, depending on the number, 
# gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). 
# Take into account cases of entering numbers from 8 and more, as well as cases of entering non-numerical data. ​

def days_of_week(user_number): 
    try:
        days_week = {1:"понеділок", 2:"вівторок", 3:"середа", 4:"четвер", 5:"п'ятниця", 6:"субота", 7:"неділя"}
        if user_number <= 0 or user_number > 7:
            raise IndexError("You enter no correct number")
        print(days_week[user_number]) 
    except ValueError:
        print("Wrong Input") 
    except TypeError as e:
            print("We obtain error:", e)   
    except IndexError as e:
        print("We obtain error:", e)

days_of_week(2)

###########################################
# def day_of_the_week (day_number):
#     try:
#         week_day_name = \
#             {1: 'Monday',
#              2: 'Tuesday',
#              3: 'Wednesday',
#              4: 'Thursday',
#              5: 'Friday',
#              6: 'Saturday',
#              7: 'Sunday'}

#         return week_day_name[int(day_number)]
#     except KeyError as e:
#         print('This key as not in list ', e)
#     except ValueError as e:
#         print('invalid literal', e)

# print(day_of_the_week(input('Enter day number: ')))
