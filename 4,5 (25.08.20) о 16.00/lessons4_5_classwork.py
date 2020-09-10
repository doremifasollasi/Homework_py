#######################################################

# This is the first part of first task ("while").The first option.
# #number = 0
# #while number < 101:
#     if number%2 == 0:
#         print(number)
#     number = number+1
# else:
#     print("These are all even numbers less than 100.")

#######################################################

# This is the first part of first task ("while"). The second option.
# number = 0
# while number <= 100:
#     print(number)
#     number+=2
# else:
#     print("These are all even numbers less than 100.")

#######################################################

# This is the second part of first task("for"). The first option.
# for number in range(101):
#     if number%2 == 0:
#         print(number)
# else:
#     print(number,"- is the last number")
# print("These are all even numbers less than 100.")

#######################################################

# This is the second part of first task("for"). The second option.
# for number in range(0,101,2):
#     print(number)
# else:
#     print(number,"- is the last number")
# print("These are all even numbers less than 100.")

#######################################################

# This is the first task (other). This is the shortest option.
# print("These are all even numbers less than 100:", list(range(0,101,2)))

#######################################################
#######################################################

# This is the second task (with continue). The first option, using loops.
# start = 0
# finish = 100
# while start <= finish:
#     if start %2 == 1: 
#         print(start)
#         start += 1
#     else:
#         start += 1
#         continue
# else:
#     print("The end!")
# print("These are all odd numbers less than 100.")

########################################################

# This is the second task (with continue). The second option, using loops. 
# for number in range(100):
#     if number % 2 == 0:
#         continue
#     print(number)
# print ("These were all odd even numbers less than 100.")

#######################################################

#This is the second task (without continue).
# for number in range(1,100,2):
#     print(number)
# else:
#     print(number,"- is the last number.")
# print("These are all odd even numbers less than 100.")

#######################################################

# This is the second task (without continue) - more short.
# odd_numbers=[number for number in range(100) if number % 2 == 1]
# print("These are all odd even numbers less than 100:", odd_numbers)

#######################################################

# This is the second task (without continue). This is the shortest option.
# print("These are all odd even numbers less than 100:", list(range(1,100,2)))

#######################################################
#######################################################

# This is third task - checking numbers for evenness and oddness. Using loops.
# for number in range(3,17):
#     print (number, "- this number is odd" if number % 2 == 1 else "- this number is even")
#     number+=1

#######################################################

# This is third task - checking numbers for evenness and oddness (usinr "break").
# contain_odd = False
# for number in range(5,25):
#     if not number % 2 == 0:
#         contain_odd = True
#         break
# if contain_odd:
#     print("There is odd nunber in the list")
# else:
#     print("There is only even number in the list")

#######################################################
#######################################################

# The fourth task. Change the data type of elements to floating point numbers ("float").
# for number in range (4,23,3):
#     print(float(number))

#######################################################
#######################################################

# The fifth task. Output Fibonacci numbers up to the entered number n, using loops. The first option.
# n = int(input("Enter some Fibonacci`s number: "))
# fibonacci_numbers = [0, 1]
# for number in range(2,n+1):
#     fibonacci_numbers.append(fibonacci_numbers[number-1]+fibonacci_numbers[number-2])
#     if fibonacci_numbers[number]==n:
#         break
# print("There are some numbers from Fibanacci till", n, "that you entered", "/n", fibonacci_numbers)

#######################################################

# The fifth task. Output Fibonacci numbers up to the entered number n, using loops. The second option.
# first_number = 0
# second_number = 1
# next_number = first_number + second_number
# n = int(input("Enter some Fibonacci`s number: "))
# if n >= 0:
#     print("There are some numbers from Fibanacci till", n, "that you entered", first_number)
#     print(second_number)
# while next_number <= n :
#     print(next_number)
#     first_number = second_number
#     second_number = next_number
#     next_number = first_number + second_number
