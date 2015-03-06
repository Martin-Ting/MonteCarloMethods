import sys, random, math
from random import *
from math import sqrt

totalTrials = 0.0
totalHits = 0.0
currError = 0.0

def trial():
    global totalTrials
    global totalHits


def printResults():
    ratio = totalHits/totalTrials
    currError = math.fabs(ratio*100 - ideal) / ideal
    print('Results ===============================')
    print('Total Trials: ', totalTrials)
    print('Number of hits: ', totalHits)
    print('Ratio: ', ratio*100)
    print('Ideal: ', ideal)
    print('Error: ', currError)
    print(' ======================================')

def main(argv):
    print("Welcome to estimating the Integral of X**2 functions");
    totalTrials=0
    totalHits=0
    for i in range(10): # 10
        trial()
    print('10')
    printResults()

    for i in range(90): # 100
        trial()
    print('100')
    printResults()

    for i in range(400): # 500
        trial()
    print('500')
    printResults()

    for i in range(500): # 1 000
        trial()
    print('1 000')
    printResults()

    for i in range(4000): # 5 000
        trial()
    print('5 000')
    printResults()

    for i in range(5000): # 10 000
        trial()
    print('10 000')
    printResults()

    for i in range(40000): # 50 000
        trial()
    print('50 000')
    printResults()

    for i in range (50000): # 100 000
        trial()
    print('100 000')
    printResults()

    for i in range (400000): # 500 000
        trial()
    print('500 000')
    printResults()

    for i in range (500000): # 1 000 000
        trial()
    print('1 000 000')
    printResults()

    for i in range (4000000): # 5 000 000
        trial()
    print('5 000 000')
    printResults()

    for i in range (5000000): # 10 000 000
        trial()
    print('10 000 000')
    printResults()

if __name__ == "__main__":
    main(sys.argv[1:])
