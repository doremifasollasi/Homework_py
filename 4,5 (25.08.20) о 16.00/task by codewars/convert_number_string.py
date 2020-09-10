# This is a task from the site "www.codewars.com"

def number_to_string(num):
    """
    A function that can transform a number into a string.
    """
    if type(num) == int:
        return str(num)
    else:
        return num + "is not number!"

################################

def number_to_string(num):
    return str(num)

################################

def number_to_string(num):
    try:
        return str(num)
    except:
        return None

################################

number_to_string = lambda n: str(n)

################################

def number_to_string(num):
    return "{}".format(num)

################################