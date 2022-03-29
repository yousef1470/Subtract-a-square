import math
number_coins=int(input("enter the number of coins you want to play with : "))
while number_coins != 0:
    while True:
        n1 = int(input("player 1: "))
        if (math.ceil(math.sqrt(n1)) == math.floor(math.sqrt(n1))) and n1<=number_coins :
            number_coins = number_coins - n1
            print("the numer of reminang coins is: " ,number_coins)
            break
    if number_coins == 0:
        print("player1 wins")
        break
    while True:
        n2= int(input("player 2: "))
        if (math.ceil(math.sqrt(n2)) == math.floor(math.sqrt(n2))) and n2<=number_coins :
            number_coins = number_coins - n2
            print("the number of reminang coins is: ", number_coins)
            break
    if number_coins == 0:
        print("player2 wins")
        break