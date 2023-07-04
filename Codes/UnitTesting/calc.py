
def add(* args):
    sum = 0
    for i in args:
        sum += i
    return sum

def multiply(x, y):
    return x * y

def subtract(x,y):
    return x - y

def divide(x,y):
    if y == 0:
        raise ValueError('You cannot divide by zero idiot!!!')
    return x / y

print(multiply(2,3))
print(add(2,3,4))
