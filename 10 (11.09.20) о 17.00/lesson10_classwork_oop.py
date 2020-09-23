# class MyClass:
#     """This is my second class"""
#     a = 10
#     def func(self):
#         print("Hello")

# obj_1 = MyClass()
# obj_2 = MyClass()
# # Output: 10
# print(obj_1.__class__.a)
# print(MyClass.__doc__)
# print(MyClass.a)
# # print(obj_2.__class__.a)

# # Output: <function MyClass.func at 0x0000000003079BF8>

# print(MyClass.func)
# print(MyClass.func(obj_1))
# print(obj_1.func)
# print(obj_1.func())

# ###############################

# class Parrot:
    
#     # class atribute
#     species = "bird"

#     # instance atribute
#     def __init__(self, name, age = 2):
#         self.name = name 
#         self.age = age 

# # instantaine the Parrot class
# blu = Parrot("Blu")
# woo = Parrot("Woo", 15)

# # access the class attributes
# print("Blu ia a {}".format(blu.__class__.species))
# print("Woo ia also a {}".format(woo.__class__.species))

# # acces the instance attributes
# print("{} is {} years old".format(blu.name, blu.age))
# print("{} is {} years old".format(woo.name, woo.age))

############################

# class Parrot: 
#     # instance attributes 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 
    
#     # instance method 
#     def sing(self, song): 
#         return "{} sings {}".format(self.name, song)
    
#     def dance(self): 
#         return "{} is now dancing".format(self.name)
        
# # instantiate the object 
# blu = Parrot("Blue", 10) 

# #call our instance methods 
# print(blu.sing("\"Happy\"")) 
# print(blu.dance())

#############################

# class Person:
#     # конструктор​
#     def __init__(self, name):
#         self.name = name # встановлюэмо ім'я

#     def __del__(self):
#         print(self.name, "deleting from memory")

#     def display_info(self):
#         print("Hello, my name is", self.name)

# person1 = Person("Tom")
# person1.display_info()  # Hello, my name is Tom​

# person2 = Person("Sam")
# person2.display_info()  # Hello, my name is Sam

# # видалення з пам’яті​
# del person1.name

# # AttributeError​
# person1.display_info()

# del person1.display_info

# # AttributeError​
# person1.display_info()

# # Deleting from memory​
# del person1

############################

# class Point3D:
#     def __init__ (self, x, y, z):
#         self.coord = (x, y, z)

#     def __repr__ (self):
#         return "Point (%s, %s, %s) " % self.coord

# P = Point3D(0.0, 1.0, 0.0)
# print(P)  # Point (0.0, 1.0, 0.0)

############

# class Line:
#      def __init__(self, p1, p2):
#          self.line = (p1, p2)

#      def __del__(self):
#          print("Removing Line %s - %s" % self.line)

# L = Line((0.0, 1.0), (0.0, 2.0))
# print(L)
# del L #Removing Line (0.0, 1.0) - (0.0, 2.0)​
# print(L)

###################

# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b

#    def __str__(self):
#       # return 'Vector (%d, %d)' % (self.a, self.b)
#       return "Vector ({}, {})".format(self.a, self.b)
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
      
# v1 = Vector(2,10)
# v2 = Vector(5,-2)

# print(v1 + v2) #Output: ​Vector (7, 8)

#############################

# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
        
#     def inputSides(self):
#         self.sides = [float(input(f"Enter side {str(i+1)}: ")) 
#                                               for i in range(self.n)]
#     def dispSides(self):
#         for i in range(self.n):
#             print(f"Side {i+1} is {self.sides[i]}")
 
#############################
           
# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 3)
#       #   super().__init__()
       
#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print(f"The area of the triangle is {area}")

# t = Triangle()
# t.inputSides() 
# t.dispSides()
# t.findArea()

##################################

# class Rectangular(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 2)
                
#     def findArea(self):
#         a, b = self.sides
#         # calculate the semi-perimeter
#         area = a*b
#         print(f"The area of the triangle is {area}")

# r = Rectangular()
# r.inputSides() 
# r.dispSides()
# r.findArea()

