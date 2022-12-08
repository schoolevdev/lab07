# Lab07vst.py
# This is a program that both bubble sorts and calculates mean, median, and standard deviation
#
import math
import random


# Procedure displayList prints the elements of list
# in a horizontal display with 20 numbers per line.
# Needed for 70-point Version.
#
def displayList(l) -> None:
    for index, item in enumerate(l):
        if index % 20 == 0:
            print()
        print(item, end=' ')
    print()


# Function getMean returns the mean of list.
# Needed for 70-Point Version.
#
def getMean(l) -> float:
    sum: int = 0
    for value in l:
        sum += value
    return sum / len(l)


# Procedure bubbleSort sorts list in ascending order.
# Needed for 80-Point Version.
#
def bubbleSort(l) -> None:
    # with n numbers there will be n-1 passes
    for k in range(len(l) - 1):
        # skip last element since there isn't an element after it
        for index, number in enumerate(l):
            if index == len(l) - 1:
                continue
            if number > l[index + 1]:
                l[index], l[index + 1] = l[index + 1], l[index]  # swap the two


# Function getMedian returns the median of list.
# Needed for 80-Point Version.
#
def getMedian(l) -> float:
    temp = l  # you may not want the original list to be sorted, so make a temp in the function
    length: int = len(temp)
    bubbleSort(temp)
    if length % 2 == 0:
        return (temp[length // 2 - 1] + temp[length // 2]) / 2
    else:
        return temp[(length + 1) // 2 - 1]


# Procedure createList generates a list of random integers
# in the (10,99) integer range.
# Seed (12345) is used to check outcome against known values.
# Needed for 100-Point Version
#
def createList(lst, length: int) -> None:  # i dont know if : list is compatible with prev versions
    random.seed(12345)
    for k in range(length):
        lst.append(random.randint(10, 99))


# Function getSD returns the Standard Deviation of list.
# Needed for the 100-Point Version.
def getSD(lst) -> float:
    mean: float = getMean(lst)
    differences = []
    for index, val in enumerate(lst):
        differences.append((lst[index] - mean) ** 2)
    diff_sum: float = sum(differences)
    variance: float = diff_sum / (len(lst) - 1)
    return math.sqrt(variance)

#######################################
# MAIN

print("TOM TERRIFIC'S LAB07 VERSION 100")
print()

# Needed for 70-Point Version.
list1 = [11,22,33,44,55,66,77,88,99]
n1 = len(list1)
displayList(list1)
print("Mean: ",getMean(list1))
print()
#

# Needed for 80-Point Version.
list2 = [11,22,33,44,55,66,77,88,99]
n2 = len(list2)
displayList(list2)
print("Mean: ",getMean(list2))
print("Median: ",getMedian(list2))
print()
#
# Needed for 80-Point Version.
list3 = [11,22,33,55,66,77]
n3 = len(list3)
displayList(list3)
print("Mean: ",getMean(list3))
print("Median: ",getMedian(list3))
print()
#

# Needed for 100-Point Version.
list4 = []
createList(list4,100)
displayList(list4)
bubbleSort(list4)
displayList(list4)     
print("\nMean:              ",getMean(list4))
print("Median:            ",getMedian(list4))
print("Standard Deviation:",getSD(list4))

