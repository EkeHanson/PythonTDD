import re

email = input('What is your email address? ')
#re.search(pattern, string, flags=0)
# . means any character except a new line
# *  means 0 or more repetitions
# + means 1 or more repetitions
# ? means 0 or 1 repetion
# {m} m prepetitions
# {m,n} m-n repetitions
# ekena
if re.search(r'.+@.+\.edu', email):
    print('Valid')
else:
    print('Invalid')