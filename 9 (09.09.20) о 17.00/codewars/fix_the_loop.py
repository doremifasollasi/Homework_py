# If you pass the list of your favourite animals to the function, 
# you should get the list of the animals with orderings and newlines added.

def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

##############################

def list_animals(animals):
    res = ''
    for i in range(len(animals)):
        res += str(i + 1) + '. ' + "".join(animals[i]) + '\n'
    return res

##############################

def list_animals(animals):
    return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))