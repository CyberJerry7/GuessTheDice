# Guess the dice game on console screen.
# developer : Cyberjerry

import random

# diceNumber = 6
# name = "Jerry"
diceNumber = random.randint(1,6)
score = 0
highScore = 0

def diceFace():
    def diceNum1():
        print("\t\t\t\t\t\t     ###########    ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t    #           #   ")
        print("\t\t\t\t\t\t    #     *     #   ")
        print("\t\t\t\t\t\t    #           #   ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t     ###########    ")

    def diceNum2():
        print("\t\t\t\t\t\t     ###########    ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t    #           #   ")
        print("\t\t\t\t\t\t    #   *   *   #   ")
        print("\t\t\t\t\t\t    #           #   ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t     ###########    ")

    def diceNum3():
        print("\t\t\t\t\t\t     ###########    ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t    #   *       #   ")
        print("\t\t\t\t\t\t    #     *     #   ")
        print("\t\t\t\t\t\t    #       *   #   ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t     ###########    ")

    def diceNum4():
        print("\t\t\t\t\t\t     ###########    ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t    #   *   *   #   ")
        print("\t\t\t\t\t\t    #           #   ")
        print("\t\t\t\t\t\t    #   *   *   #   ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t     ###########    ")

    def diceNum5():
        print("\t\t\t\t\t\t     ###########    ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t    #   *   *   #   ")
        print("\t\t\t\t\t\t    #     *     #   ")
        print("\t\t\t\t\t\t    #   *   *   #   ") 
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t     ###########    ")

    def diceNum6():
        print("\t\t\t\t\t\t     ###########    ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t    #   *   *   #   ")
        print("\t\t\t\t\t\t    #   *   *   #   ")
        print("\t\t\t\t\t\t    #   *   *   #   ")
        print("\t\t\t\t\t\t    ##         ##   ")
        print("\t\t\t\t\t\t     ###########    ")

    if(diceNumber == 1):
        diceNum1()

    elif(diceNumber == 2):
        diceNum2()    

    elif(diceNumber == 3):
        diceNum3()    

    elif(diceNumber == 4):
        diceNum4()

    elif(diceNumber == 5):
        diceNum5()

    elif(diceNumber == 6):
        diceNum6()

    else:
        print("Error")    

print("\n\n\n \t \t \t \t \t    >>> - Guess the dice - <<< \n \n \n")

name = input("Dear user, Enter your good name: ")

print("\n\n\n***************************************************\n\n\n")

print("\n\n\n \t \t \t \t \t    >>> - Guess the dice - <<< \n \n \n")

print("Hey", name, ", you will have to guess the number of the dice. \n")
print("If you get it right, your score will increase by 1")
print("If you get it wrong, your score will be reset to 0")
print("Enjoy the game and break you own records ;)\n")
abc = input("Enter any key to continue... ")


def scores():
    print("\n\n\n***************************************************\n\n\n")
    print("\n\n\n \t \t \t \t \t    >>> - Guess the dice - <<< \n \n \n")

    print("Name: ",  name,)
    print("Score: ",  score)
    print("High Score: ",  highScore)
    print("\n")

while True:

    scores()

    userGuess = int(input("Guess the dice : "))

    if (userGuess>6 or userGuess<1):
        while(userGuess>6 or userGuess<1):
            
            scores()
            print("Choose numbers between 1 to 6")
            userGuess = int(input("Guess the dice : "))

    if (userGuess == diceNumber):
        
        if(highScore == score):
            highScore = highScore + 1

        score = score + 1

        scores()
        diceFace()

        print("Correct guess!!! +1 point")
        abc = input("Enter any key to continue. To exit, type \"exit\"...")

    elif (userGuess != diceNumber):
        score = 0

        scores()
        diceFace()

        print("Wrong guess!!! Points : 0")
        abc = input("Enter any key to continue. To exit, type \"exit\"... ")

    if (abc == "exit"):
        break

    print("\n\n\n")