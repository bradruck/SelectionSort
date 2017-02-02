# Selection Sort Run-Times, Assignment #7 - P12.2
# Programmer: Bradley Ruck
# CSC 217 470
# Date Created: 7/21/2016
# Date of Final Update: 7/22/2016

# A selection sort algorithm that accepts user input for a range of number of random elements in a list
# (minimum and maximum) as well as a user defined number of sample runs to perform. The results
# of the runs, in the form of seconds to complete, are collected in a 2-dimensional array. Finally,
# the results are printed in tabular form utilizing a separate GUI window.
#
# Variables/Definitions used:   selectionSort - function that returns a ascending sorted list
#                               minimumPosition - function that returns the value of the smallest element in a list
#                               tableArray - list that holds a 2-dimensional array of the results (sort size, sort time)
#                               values - list of elements to be sorted
#                               minPos - position of the minimum element in the list
#                               nmin, nmax, runs - user provided data for minimum sort size, maximum sort size, and
#                                                  number of sample sorts to execute
#                               startTime, endTime - starting and ending times of the sort
#

from random import randint
from time import time
from tkinter import *

tableArray = []     # A list to hold a two dimensional array used to store the values of sort sizes and
                    # corresponding sort times

# Function to execute a selection sort of a list
#
def selectionSort(values) :
    for i in range(len(values)) :
        minPos = minimumPosition(values, i)
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp


# Function to find smallest element in tail range of list
#
def minimumPosition(values, start) :
    minPos = start
    for i in range(start +1, len(values)) :
        if values[i] < values[minPos] :
            minPos = i

    return minPos

# Main driver program to measure length of time to sort a user defined list using the selection sort algorithm
#
def main() :
    # Prompt for the minimum sort size
    print()
    nmin = int(input("Enter the minimum list size: "))

    # Prompt for the maximum sort size
    print()
    nmax = int(input("Enter the maximmum list size: "))

    # Prompt for the number of measurements
    print()
    runs = int(input("Enter the number of different measurements to run: "))

    n = nmin

    for i in range(runs) :
        # Construct the random list to sort
        #
        values = []
        for x in range(n):
            values.append(randint(1, 1000))

        # Get the time at the start of the sort, sort, then get the time at the end of the sort
        #
        startTime = time()
        selectionSort(values)
        endTime = time()

        # Collect the sort sizes and sort times into a two dimensional array
        #
        tableArray.append([n, round((endTime - startTime), 3)])

        # The sort sizes are stepped up at even increments based on max, min and number of sorts provided by user
        #
        n = int(n + ((nmax - nmin) / (runs - 1))) - int(n + ((nmax - nmin) / (runs - 1))) % 5

    # Create a new GUI window and display the results in tabular form
    #
    window = Tk()
    window.title("Results of Sample Runs - Selection Sort")
    t1 = Label(text='Sort Size')
    t2 = Label(text='Seconds to Sort')
    t1.grid(row=0, column=1, sticky=NSEW)
    t2.grid(row=0, column=2, sticky=NSEW)
    for i in range(runs):
        l1 = Label(text='%.0f' % tableArray[i][0], relief=RIDGE, width=20, height=2)
        l2 = Label(text='%.3f' % tableArray[i][1], relief=RIDGE, width=20, height=2)
        l1.grid(row=i+1, column=1, sticky=NSEW)
        l2.grid(row=i+1, column=2, sticky=NSEW)
    window.mainloop()

# Run the main program
#
main()
