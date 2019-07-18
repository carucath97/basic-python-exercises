#Partial Functions

from functools import partial

def multiply(x , y):
    return x * y

double = partial(multiply, 2)
triple = partial(multiply, 3)

a = 5
b = double(a)
c = triple(a)

print(b, "is double the value of", a,"\n", c, "is triple to", a)
