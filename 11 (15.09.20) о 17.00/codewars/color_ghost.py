from random import choice

class Ghost(object):   
    '''This is a class Ghost. Ghost objects are instantiated without any arguments.
    Ghost objects are given a random color attribute of 
    "white" or "yellow" or "purple" or "red" when instantiated'''
    def __init__(self):
        colors = ["white","yellow","purple","red"]
        self.color = choice(colors)

######################

from random import choice

class Ghost(object):
    def __init__(self):
        self.color = choice(["white",
                            "yellow",
                            "purple",
                            "red"])

######################

import random
class Ghost(object):

    colors = ["white", "yellow","purple","red"]

    def __init__(self):
        self.color = random.choice(Ghost.colors)

######################

import random

class Ghost(object):   
    
    def __init__(self):
        colors = ("white","yellow","purple","red")
        self.color = random.choice(colors)

######################

import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])