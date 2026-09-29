#Name script file: loopl.py
#This script rool dice ten times
from random import randint
import os

def rollDice():
    i = 1
    while i <= 10:
        key = input("press any key to roll dice :::")
        print(f"::: Rool {i} :::")
        print(f"Dice 1:{randint(1,6)}")
        print(f"Dice 2:{randint(1,6)}")
        print("\n")
        i+=1
rollDice()