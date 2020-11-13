from sllist import SingleLinkedList

def average(list):
    length = list.size()
    sum = 0
    templist = list
    while not templist.isEmpty():
        sum += templist.head()
        templist = templist.tail()
    return sum/length