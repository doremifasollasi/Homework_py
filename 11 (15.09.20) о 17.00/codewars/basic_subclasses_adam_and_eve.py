class Human:
    '''This is class Human'''
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

    def gender(self):
        return 'Man'

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)
        
    def gender(self):
        return 'Woman'
    
first_man = Man("Adam")
first_woman = Woman("Eve")

def God():
    people = (first_man, first_woman)
    return people

###########################

def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass
    
class Woman(Human):
    pass

############################

class Human(object):
    def __init__(self):
        pass

class Man(Human):
    def __init__(self, name):
        self.name = name

class Woman(Human):
    def __init__(self, name):
        self.name = name

def God():
    adam = Man('Adam')
    eva = Woman('Eva')
    return [adam, eva]