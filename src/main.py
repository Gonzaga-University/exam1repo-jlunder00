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

if __name__ == "__main__":
    print("Starting program")

    adder = Adder(10, 20)
    print(adder.getSum())
    
    print(adder.getSumMoreThanOnce(10)

    print("Done with program")
