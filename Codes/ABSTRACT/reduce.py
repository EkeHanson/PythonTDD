import functools

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y: x*y, factorial)
print(result)

word = ['H','E', 'L', 'L','O']
word = functools.reduce(lambda x,y: x+y, word)
print(word)