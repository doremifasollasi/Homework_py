# # Draft, reflections

# # count_sticks = 21
# count_sticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# for i in range(20):
#     players_move = int(input('You can take turns taking 1, 2, or 3 sticks. How many sticks do you take? '))
#     count_sticks -= players_move
#     if count_sticks <= 1: 
#         return 'You win'

# len(count_sticks)-=players_move
# make_move()

# # ###################

# # Draft, reflections. It works
# count_sticks = 4
# players_move = int(input('You can take turns taking 1, 2, or 3 sticks. How many sticks do you take? '))
# count_sticks -= players_move
# if count_sticks <= 1: 
#     print('You win')

# ###############

# # Draft, reflections
# import random
# if sticks % 4 != 0:
#     return sticks % 4 
# else:
#     return random.randint(1,3)

########################

# # Draft, reflections
# def make_move(sticks):
#     return 'To be in a winning position, take {} sticks'.format(sticks % 4)

# ####################

# # Draft, reflections
# def make_move(sticks):
#     return 'To be in a winning position, take {} sticks'.format(sticks % 4)

# print (make_move(6))

##########################

# solution of the task

def make_move(sticks):
     '''In this game, there are 21 sticks lying in a pile.
     Players take turns taking 1, 2, or 3 sticks. The last person to take a stick wins.
     A robot that will always win the game. Your robot will always go first. 
     The function should take an integer and returns 1, 2, or 3.
     Note: The input will always be valid (a positive integer)'''
     while sticks > 0:
         return sticks%4

print(make_move(5))

#########################
#########################

# print('21 sticks in the pile')
# pile = 21

# while pile > 0:
#     player_name = input('Name: ')
#     sticks = int(input('Make move: '))
#     pile = pile-sticks
#     print(f'{player_name} takes {sticks} --> {pile} sticks left')

# print(f'{player_name} takes {sticks} --> {player_name} wins!')