import random
import os, time

money = 10000

def gamble(guess):

    if guess != "red" or guess != "show" or guess != "black" or guess != "zero":
        print("enter a REAL command next time...")
        time.sleep(1)
        os.system("cls")
        return None

    global money
    value = random.randrange(0, 38)

    #show amount of money
    if guess == "show":
        print("you have " + str(money) + " to spend. \nits the next big spin! why dont you go all in!")
        time.sleep(2)
        os.system("cls")
        return None 

    #zero
    if value == "zero" and value == 0:
        money = money * 10000
        print("you somehow beat the 1/37 odds. your money has multiplied by 10000x.\nyour cuurent amount is " + str(money) + ".")
        time.sleep(2)
        os.system("cls")
        return None
    
    #red
    if guess == "red" and value % 2 == 0:
        money = money * 2
        print("congratulations! you just 2x'ed your money!!! \nyour current balance is "  + str(money) + ".")
        time.sleep(2)
        os.system("cls")
        return None

    #black
    if guess == "black" and value % 2 != 0:
        money = money * 2
        print("congratulations! you just 2x'ed your money!!! \nyour current balance is "  + str(money) + ".")
        time.sleep(2)
        os.system("cls")
        return None
    
    #exit
    exit("you lost all your money bwah bwah.")


                                                                                                            


while True:
    gamble(input("hey guys!! \nlets instill a gambling addiction by playing this game!!! \nblack, red or zero? if you win on zero, you 10000x you 10000x your money!!!! \nbut thats only a 0.027%% chance of happening!!\noh yeah, do show to show balance."))
    