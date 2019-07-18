#Unique Sum

def unique_sum(int1, int2, int3):
    if(int1 == int2 == int3):
        return 0
    elif(int1 == int2 != int3):
        return int3
    elif(int1 == int3 != int2):
        return int2
    elif(int2 == int3 != int1):
        return int1
    else:
        return(int1 + int2 + int3)

unique_sum(3, 3, 3)
unique_sum(3, 3, 4)
unique_sum(1, 3, 3)
unique_sum(3, 2, 3)
unique_sum(56, 7, 28)


