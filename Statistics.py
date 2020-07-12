from collections import Counter
import math
print("Hello. \nIt's  programm to find the:\n1.Mean\n2.Median\n3.Mode\n4.Range\n5.Standart deviation of data sets")
i = 0 #counter
numbers = list()
length = int(input(("How many numbers do you want to enter?: ")))
#for sum of set
def listsum(numList = numbers):
    theSum = 0
    for a in numList:
        theSum = theSum + int(a)
    return theSum

def Mean():
    mean = listsum() / length
    return mean
def Median():
    middle = float(length)/2
    if middle % 2 != 0:
        return numbers[int(middle - .5)]
    else:
        mid = numbers[int(middle)]
        mid2 = numbers[int(middle-1)]
        result = (int(mid) + int(mid2)) / 2
        return result
def Mode():
    a = numbers

    a_set = set(a)

    most_common = None
    qty_most_common = 0

    for item in a_set:
        qty = a.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item

    return (most_common)
def Range():
    result = int(max(numbers)) - int(min(numbers))
    return result
def StandardDeviation():
    stepOne = []
    theSum = 0
    for a in numbers:
        number = int(a) - Mean()
        number = pow(number,2)
        stepOne.append(number)
    theSum = listsum(stepOne)
    theSum = theSum / (length - 1)
    result = math.sqrt(theSum)
    result = round(result, 2)
    return result

while i != length:
    numbers.append(input("Insert the number: "))
    i = i + 1
print("------------------------------------------------------------------------------------------------------------------------")
print("Sum: ",listsum())
print("1.Mean:",Mean())
print("2.Median:",Median())
print("3.Mode:",Mode())
print("4.Range:",Range())
print("5.Standard Deviation:",StandardDeviation())
input("Press any key for exit")



