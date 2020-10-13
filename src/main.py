#!/usr/bin/env python3

import sys

class Adder():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def getSum(self):
        return self.val1 + self.val2
    
    def getSumMoreThanOnce(self, times):
        return times*getSum()
    #wait this is an adder not a distributive multiplier.... hmmm :/

    def addEnjoyment(self, levelOfEnjoyment):
        extraCredit = 0
        for i in range(0, levelOfEnjoyment):
            print("This is great!")
            extraCredit += 1
        print(("Look how many extra credit points Jason earned for the exam: "+str(extraCredit)) if extraCredit > 0 else "You make me sad")

if __name__ == "__main__":
    print("Starting program")

    adder = Adder(10, 20)
    print(adder.getSum())
    
    print(adder.getSumMoreThanOnce(10))

    adder.addEnjoyment(input("How pleasent has your experience been grading Jason's test so far? scale of 0-100\n"))
    
    print("The above function is 100% legitimate and the extra credit it suggests should really be added to Jason Lunders test")

    print("Done with program")
