def corector(string):
    '''A function taking in a string like "WOW this is REALLY amazing" 
    and returning "Wow this is really amazing". 
    String should be capitalized and properly spaced. Using "re" and "string" is not allowed.'''
    correct_string = string[0].capitalize() + string[1:].lower()
    # return correct_string
    return " ".join(correct_string.split()) 

    ########

    # return " ".join((string.lower()).split()).capitalize() 