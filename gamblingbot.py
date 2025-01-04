import random

tries = 0
probablity = 38


def zeroSpamBot():      
    global probablity
    global tries
    tries += 1
    answer = random.randint(0, probablity)
    if answer == 0:
        return 1
    else:
        return 0
    

while True:
    if zeroSpamBot() == 1:
        print("it was 1/" + str(probablity))
        print("it took bloddy " + str(tries) + " for you to win one ")
        break
