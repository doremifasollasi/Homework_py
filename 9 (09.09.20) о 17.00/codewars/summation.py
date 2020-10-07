def summation(num):
    '''This is a program that finds the summation of every number from 1 to num. 
    The number will always be a positive integer greater than 0.'''
    total = 0
    for x in range(1, num+1) : 
        total = total + x
    return total 
    
# ######################

def summation(num):
    return sum(range(num + 1))

#########################

def summation(num):
    return (1+num) * num / 2

###########################

def summation(num):
    return num*(num+1)//2