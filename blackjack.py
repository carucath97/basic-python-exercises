#BlackJack (and hookers...)

def blackjack(int1, int2):
    if(int1 < 0 or int2 < 0):
        return("Error!")
    # return an error since a negative number has been entered
    elif(int1 > 21 and int2 > 21):
        return 0
    # return 0 as they are both over 21
    elif(int1 > 21 and int2 <= 21):
        return int2
    # return int2 by default as int1 is over 21
    elif(int1 <= 21 and int2 > 21):
        return int1
    # return int1 by default as int2 is over 21
    elif(int1 > int2):
        return int1
    # return int1 as it's closer to 21
    elif(int1 < int2):
        return int2
    # return int2 as it's closer to 21
    else:
        return("It's a tie!")
    # declare a tie as the numbers are identical

blackjack(-1, 21)
blackjack(21, 13)
blackjack(22, 23)
blackjack(21, 22)
blackjack(15, 15)
blackjack(13, 11)