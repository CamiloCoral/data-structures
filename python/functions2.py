#Functions with return and without params
from random import randint
import os
def roolDice():
    die1=randint(1,6)
    die2=randint(1,6)
    return die1,die2

#main
dice = roolDice()
print(f"Dice:{dice}")
if dice[0]== 6 and dice[1]==6 :
    print("you win!!!")
else :
    print("Try again!")
