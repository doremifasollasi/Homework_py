# This is a task from the site "www.codewars.com"
def greet(name):
    """ 
    Jenny was all hyped by the possibillity Johnny might check her web app
    so she made a mistake by returning the result before checking if Johnny
    is one of the users logging to her web app. Silly girl!
    We corrected the function by adding an else statement.
    """
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"

########################################

def greet(name):
    if name != 'Johnny':
        return "Hello, {name}!".format(name=name)
    else:
        return "Hello, my love!"
########################################

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

########################################

def greet(name):
    return "Hello, {name}!".format(name = ('my love' if name == 'Johnny' else name))

########################################

def greet(name):
    return "Hello, {name}!".format(name=name.replace("Johnny", "my love"))    

########################################

def greet(name):
    return "Hello, {}!".format((name, "my love")[ name == "Johnny"])

########################################

def greet(name):
    return "Hello, my love!" if name == 'Johnny' else "Hello, {name}!".format(name=name)

########################################

def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"

########################################

def greet(name):
    return f"Hello, {'my love' if name == 'Johnny' else name}!"    

########################################

greet = lambda name: "Hello, " + ("my love" if name == "Johnny" else name) + "!"

########################################

greet = lambda n: "Hello, {}!".format(n.replace("Johnny","my love"))

########################################

def greet(name):
    Johnny = 'my love'
    return f'Hello, {Johnny if name=="Johnny" else name}!'