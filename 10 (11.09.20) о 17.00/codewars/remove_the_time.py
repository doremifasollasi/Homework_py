def shorten_to_date(long_date):
    '''A function, shortenToDate, that takes the Website date/time 
    in its original string format, and returns the shortened format.'''
    short_date = long_date.split(',')
    return short_date[0]

################

def shorten_to_date(long_date):
    return long_date.split(',')[0]

###############

def shorten_to_date(long_date):
    return long_date[:long_date.index(',')]

#################

def shorten_to_date(long_date):
    return long_date[:long_date.rfind(',')]

#################

def shorten_to_date(long_date):
    index = long_date.index(',')
    new_string = long_date[:index]
    return (new_string)