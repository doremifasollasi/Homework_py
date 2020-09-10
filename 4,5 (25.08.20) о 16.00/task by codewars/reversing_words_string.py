# This is a task from the site "www.codewars.com"
  
def rev_sentence(sentence): 
    """
    This a function that reverses the words in a given string.
    A word can also fit an empty string.
    """
    # first split the string into words 
    words = sentence.split(' ')  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words))  
    # finally return the joined string 
    return reverse_sentence   

###############

def func_reverse(st):
    words = st.split(" ")
    revers_sentence = " ".join(reversed(words))  
    return revers_sentence

##############

 def reverse(str):
    return str((' '.join(list(str.split())[::-1])))

##############

def reverse(st):
    return ' '.join(reversed(st.split()))

################

def reverse(st):
    x = st.split()
    x = list(reversed(x))
    return (" ".join(x))

##################


def reverse(st):
    st = ' '.join(st.strip().split(' ')[::-1])
    return st

reverse('Hello World') == 'World Hello'
reverse('Hi There.') == 'There. Hi'

###############

def reverse(st):
   return st[::-1]
print(reverse("OLGA"))    

###################

def reverse(st):
  return reversed(st.split(st))
print(reverse('Hello World'))

###################

def reverse(st):
    a = st.split()
    a = list(a[::-1])
    return (' '.join(a))
print(reverse('Hello World'))