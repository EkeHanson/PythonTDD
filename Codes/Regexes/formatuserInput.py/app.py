# import re
# name = input("What's your name? ").strip()
# matches = re.search("^(.+), *(.+)$", name)
# if matches:
#     name = matches.groups(2) + " " + matches.groups(1)
# print(f"Hello, {name}")


import re
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    name = matches.groups(2) + " " + matches.groups(1)
print(f"Hello, {name}")


