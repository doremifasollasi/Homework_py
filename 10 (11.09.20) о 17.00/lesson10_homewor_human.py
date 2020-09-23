# Create a class Human, everyone has a name, 
# create a method in the class that displays a welcome message to a each person. 
# Create a class method in the class that returns information that it is a species of "Homosapiens". 
# And also in the class create a static method that returns an arbitrary message. ​

class Human:
    '''This is class Human'''

    # class atribute
    species = "Homosapiens"

    # instance atribute
    def __init__(self, name):
        self.name = name
    
    def message(self):
        return 'Welcome, {}!'.format(self.name)

    # instance method
    def say(self, word):
        self.word = word
        return "{name} usualy begins the conversation with words: '{word}'".format(name = self.name, word = self.word)
    
    # Instead of accepting a self parameter, 
    # class methods take a 'cls' parameter that points to the class —
    # and not the object instance — when the method is called.
    @classmethod
    def get_species(cls):
        return cls.species

    # To create a static method @staticmethod decorator is used (only "new" classes can have static methods):​
    # They do not receive neither an instance (self) nor class (cls) as the first parameter.
    @staticmethod
    def pulse(name):
        return f"The {name}'s heart is beating"


person_1 = Human("Marko")
print(person_1.say("What's up?"))     
person_2 = Human("Marfa")
print(person_2.say("How are you?"))  

print(person_1.get_species()) 
print(person_2.get_species()) 

Human.species = "Mammal"
print(person_1.get_species()) 
print(person_2.get_species()) 

print(person_1.pulse('Marko'))
print(person_2.pulse("Marfa"))
