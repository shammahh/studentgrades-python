
from operator import index, indexOf
import random

def average(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        ave = sum / len(arr)
    return ave
        
        
averagetest = [4, 5, 1, 2, 9, 7, 10, 8]


stugrades = []
i = 0
while i < 35:
    x = random.randint(1, 100)
    stugrades.append(x)
    i += 1


loop = True
while loop:
    print("----------------------------------------------")
    print("1 - Display All Grades")
    print("2 - Display Honours")
    print("3 - Stats")
    print("4 - Randomize Grades")
    print("5 - Exit")
    ### menu timee
    runfun = int(input("Enter seelection 1-5:"))
    if runfun == 1:
        ### generate 35 numbers between 1 - 100
            print("ALL GRADES")
            for i in stugrades:
                print(i)
    elif runfun == 2:
        n = 0
        for i in stugrades:
            if i > 80:
                print(i)
                n += 1
        print("The number of Honours is: ")
        print(n)
    elif runfun == 3:
        ## Average function returns 5.75 with average-test-Array
        biggrades = str(max(stugrades))
        smallgrades = str(min(stugrades))
        avegrade = str(average(stugrades))
        print("STATS")
        print("The highest grades is:  " + biggrades)
        print("The lowest grade is:  " + smallgrades)
        print("The grade average is:  " + avegrade)
    elif runfun == 4:
        stugrades.clear()
        i = 0
        while i < 35:
            x = random.randint(1, 100)
            stugrades.append(x)
            i += 1
        for i in stugrades:
                print(i)
    elif runfun == 5:
        loop = False
        print("goodbye :)")