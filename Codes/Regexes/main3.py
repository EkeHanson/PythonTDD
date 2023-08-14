import re

email = input('What is your email address? ')
#[a-z] include all characters
#[^@] include all characters except the @
# ? means 0 or 1 repetion
# ^ matches the start of a string
# $ matches the end of the string or just before the newline at the end of the string
if re.search(r'^[a-zA-Z0-9_]+@+[a-zA-Z0-9_]+\.edu$', email):
    print('Valid')
else:
    print('Invalid')