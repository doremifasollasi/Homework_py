import re

def passValidator (passCheck):
    if  re.search(r"[a-z]", passCheck) \
        and re.search(r"[A-Z]", passCheck) \
        and re.search('$|#|@', passCheck) \
        and 5 < len(passCheck) < 17:
        return "The password is appropriate"
    else:
        new_try = input('Enter valid pass: ')
        passValidator(new_try)