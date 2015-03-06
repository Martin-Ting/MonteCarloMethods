import sys, random, math
from random import *
from math import sqrt

MAXVAL=1000.0

totalTrials = 0.0
totalHits = 0.0
currError = 0.0

# a trial represents a single simulation
def trial():
    global totalTrials
    global totalHits
    x=randint(-MAXVAL, MAXVAL)/MAXVAL
    y=randint(-MAXVAL, MAXVAL)/MAXVAL

    totalTrials+=1.0

    if sqrt(x*x + y*y) <= 1.0:
        totalHits += 1.0

def printResults():
    currError = math.fabs((4.0*totalHits/totalTrials) - math.pi) / math.pi
    print('Results ===============================')
    print('Total Trials: ', totalTrials)
    print('Number of hits: ', totalHits)
    print('Ratio: ', 4.0*totalHits/totalTrials)
    print('Ideal: ', math.pi)
    print('Error: ', currError)
    print(' ======================================')

def main(argv):
    print("Welcome to estimating Pi");
    print("We will first run 10 trials");

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

    print('Note: Multiplication error may apply')

if __name__ == "__main__":
    main(sys.argv[1:])
