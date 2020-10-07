def sorter(textbooks):
    '''Function that sort a list full of textbooks by subject'''
    return sorted(textbooks,key=str.lower)

########################

def sorter(textbooks):
    return sorted(textbooks, key = lambda arg: arg.lower())

########################

def sorter(lst):
    return sorted(lst, key=lambda e: e.lower())