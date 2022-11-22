import random
import numpy as np
import matplotlib.pyplot as plt

def bubblesort(mylist):

    comparisons = 0
    # You have to go through the list n times.
    for i in range(len(mylist)):

        # Each time through the list, it might turn out
        # to be sorted already. You can tell it's sorted
        # if the number of swaps made is 0.
        swaps = 0

        # You'll compare each element with the element
        # that comes next, and swap if the former > the latter.
        # That's why you stop at len(mylist)-1
        # And since each time you go through, you fix the another
        # position at the end, you only need to go up to
        # len(mylist)-i-1
        for j in range(len(mylist)-i-1):

            # if the current item > next item swap them
            comparisons +=1
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
                swaps += 1
        # If you get all the way through with no swaps
        # the list is sorted, so you can quit.
        if swaps == 0:
             return 

def selectionsort(mylist):

    # The last element will automatically
    # be right after you find the correct
    # element for the second to last element
    # so you can skip it.
    comparisons = 0
    for i in range(len(mylist)-1):

        # Keep track of the minimum value and
        # the index of the minimum value.
        minval = mylist[i]
        minindex = i

        # When you find something smaller than the current
        # mininum, set it as the new minimum.
        for j in range(i+1, len(mylist)):
            comparisons += 1
            if mylist[j] < minval:
                minval = mylist[j]
                minindex = j

        # Swap the new minimum with whatever is in the
        # current position, i.
        temp = mylist[i]
        mylist[i] = mylist[minindex]
        mylist[minindex] = temp


def main():

    # Here is some test code for you to
    # test your print statements that you
    # add in Part 2, Step 3
    # You won't include this code in your
    # program. It's just an example.
    testlist = [1, 5, 2, 10, 7, 11]
    testlist2 = testlist.copy()
    bubblesort(testlist)
    selectionsort(testlist2)

    # Implement this pseudocode below.

    # declare bubblelist, selectionlist as empty lists
    # declare counter as an int equal to 0
    # while counter < 1000
       # create list of length 10 containing ten random ints
       #     between 1 and 100 (duplicates are okay)
       # make a copy of that list (use the copy() function)

       # submit the first copy of the list to bubblesort()
       # append the result to bubblelist

       # submit the second copy of the list to selectionsort()
       # append the result to selectionlist

    # print min, max, average of bubblelist
    # print min, max, average of selectionlist

    # create a plot with two subplots
    # plot histogram of bubblelist with appropriate labels
    # plot histogram of selectionlist with appropriate labels




main()
