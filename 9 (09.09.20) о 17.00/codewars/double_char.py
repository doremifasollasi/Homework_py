# Given a string, you have to return a string in which each character (case-sensitive) 
# is repeated once.
def double_char(s):
    new_string = ""
    for char in s:
        char = char*2
        new_string += char 
    return new_string

###########################

def double_char(s):
    return ''.join(c * 2 for c in s)

###########################

def double_char(string):
    return "".join(ch+ch for ch in string)