#User Input

value = int(input("Pick a number"))

def populate_list(list_length):
    new_list = []
    for iteration in range(list_length):
        new_list.append(iteration + 1)
        print(iteration + 1)
    print(new_list)
    multiply_list(new_list)

def multiply_list(created_list):
    for iteration in range(len(created_list)):
        print(created_list[iteration] * 10)

populate_list(value)