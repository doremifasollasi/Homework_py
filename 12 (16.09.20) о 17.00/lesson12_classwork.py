# vec1 = [3, 10, 2]
# vec2 = [-20, 5, 1]
# # vec3 = [6, 55, 4, 21]
# dot_mul = [u*v for u, v in zip(vec1, vec2)]
# print(zip(vec1,vec2))
# print(list(zip(vec1,vec2)))
# # print(list(zip(vec1,vec2,vec3)))
# print(dot_mul)
# print(sum(dot_mul))

#############
#############

# CLASSWORK TASK FIRST

# names = ['Sam', 'Don', 'Daniel']
# for i in range(len(names)):
#     names[i] = hash(names[i])
# print(names)

# names = ['Sam', 'Don', 'Daniel']
# # hash_list = map(hash, names)
# # print(list(hash_list))
# print(list(map(hash, names)))

#############
#############

# CLASSWORK TASK SECOND

# All these numbers in the list have a string data type, 
# for example ['1', '2', '3', '4', '5', '7'], 
# convert this list to a list, all numbers of which have the data type integer: 
# 1) using the append method 2) using the map method

# str_list = ['1', '2', '3', '4', '5', '7']
# int_list = map(int, str_list)
# print(list(int_list))

# new_list = []
# for i in str_list:
#     new_list.append(int(i))
# print(new_list)

#############
#############

# CLASSWORK TASK THIRD
# Convert list containing miles to list containing kilometers (1 mile = 1.6 kilometers) 
# a) using the map function b) using the map and lambda function 

# list_mile = [1,2,3,4,5]
# list_kilom = map(lambda x: round(x*1.6, 2), list_mile)
# print(list(list_kilom))

# #############

# def miles_to_kilometers(num_miles):
#     return round(num_miles*1.6,2)
# mile_distances = [1.0, 6.5,17.4]
# kilometer_distances = list(map(miles_to_kilometers,mile_distances))
# print(kilometer_distances)

#############
#############

# def createGenerator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i

# mygenerator = createGenerator() # create generator
# print(mygenerator) # mygenerator is object

# print('First call')
# for i in mygenerator:
#     print(i)
# print('Second call')
# for i in mygenerator:
#     print(i)

#############
#############

# ​HOMEWORK TASK
# Create a simple generator function similar to the range iterator.​

generator_range = (i for i in range(11))

print(generator_range)