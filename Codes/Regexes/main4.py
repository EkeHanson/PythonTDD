import re

email = input('What is your email address? ')
# \d decimal digit
# \D not decimal digit
# \s whitespace characters
# \S not a whitespace character
# \w word character ..as well as numbers and the underscore
# \W not a word character
# A|B means either A or B
# (...) a group
# (?:...) non-capturing version
# re.MULTILINE
# re.DOTALL
# if re.search(r'^[\w|\s]+@+\w+\.(edu|gov|com|org|net)$', email): # this includes a whitespace in it's expression
# if re.search(r'^\w+@+\w+\.(edu|gov|com|org|net)$', email, re.IGNORECASE):
if re.search(r'^\w+@(\w+\.)?+\w+\.(edu|gov|com|org|net)$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')