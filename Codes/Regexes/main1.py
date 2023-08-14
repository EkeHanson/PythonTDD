import re

email = input('What is your email address? ')
# ^ matches the start of a string
# $ matches the end of the string or just before the newline at the end of the string
if re.search(r'^.+@.+\.edu$', email):
    print('Valid')
else:
    print('Invalid')