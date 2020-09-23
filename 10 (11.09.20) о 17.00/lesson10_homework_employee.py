# Create an employee class. Each employee has characteristics such as name and salary. 
# The class should have a counter that calculates the total number of employees, 
# as well as a method that prints the total number of employees 
# and a method that displays information about each employee in particular, namely the name and salary.​

# In addition to creating a class, 
# display information about the base classes from which the employee class is inherited (__base__), 
# the class namespace (__dict__), the class name (__name__), 
# the module name in which the class is defined (__module__), the documentation bar ( __doc__) ​

class Employee():
    '''It is class of an employee. 
    Where are each employee has characteristics such as name and salary.'''

    counter_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter_employees += 1

    def counter(self):
        return f'The total number of employees {Employee.counter_employees}.'

    def inform(self):
        return f"{self.name}'s salary is {self.salary}."

empl_1 = Employee("Anna", 20)
print(empl_1)

print(f'INFORMATION ABOUT the employee class is inherited from {Employee.__base__}, \n the class namespace is {Employee.__dict__}, \n the class name is {Employee.__name__}, \n the module name in which the class is defined is {Employee.__module__}, \n the documentation bar is : {Employee.__doc__}.')

# #################################

# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def __repr__(self):
#         return f"Ma name is {self.name}. I am {self.age} years old. I am {self.gender}."

# class Employee(Human):
#     def __init__(self, name, age, gender, salary, position, science_degree):
#         # super().__init__(name, age, gender)
#         Human.__init__(self, name, age, gender)
#         self.position = position
#         self.salary = salary
#         self.science_degree = science_degree
    
#     def get_position(self):
#         return self.position

# # спершу викличиться метод __new__, потім він смикне конструктор, який засетить ці три значення
# t_1 = Human("Olena", 15, "Female")
# print(t_1)

# em_1 = Employee('Stepan', 22, "Man", 1500, 'teacher', 'assotiate profesor')
# print(em_1.get_position())

# print(Employee.__mro__)