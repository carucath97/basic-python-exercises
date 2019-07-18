print("Hello World")

#Assignment

hello_world = "Hello World"
print(hello_world)

#Parameters
def print_word(string):
    print(string)
    
print_word("Hello")
print_word("Banana!")

#Parameters/Operators
def sum_num(num1, num2):
    print(num1 + num2)
    
sum_num(1, 2)
sum_num(7655, 353451)

#Conditionals
def sum_number(num1, num2, is_tall):
    if (num2 > 0 and is_tall):
        return(num1 + num2)
    else:
        return(num1 * num2)
        
print(sum_number(1, 2, True))
print(sum_number(32, 56, False))
        
#Conditionals2
def num(num1, num2, is_tall):
    if (num2 > 0 and is_tall):
        return (num1 + num2)
    elif (num1 == 0 and num2 != 0):
        return num2
    elif (num1 != 0 and num2 == 0):
        return num1
    else:
        return (num1 * num2)
        
print(num(3, 5, True))
print(num(0, 6, False))
print(num(0, 0, True))


