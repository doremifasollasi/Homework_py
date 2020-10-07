# A method to see whether the string is ALL CAPS.

def is_uppercase(inp):
    new_inp = ''
    for char in inp:
        if char == char.upper():
            new_inp += char
    if len(inp) == len(new_inp):
        return True
    else:
        return False

#######################

def is_uppercase(inp):
    return inp.isupper()

######################

def is_uppercase(inp):
    return inp.upper()==inp

####################

def is_uppercase(inp):
    if inp.isupper():
        return True
    else:
        return False

##################

def is_uppercase(inp):
    from re import search
    if search(r'[a-z]', inp):
        return False
    return True