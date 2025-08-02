from typing import List

# we iterate through whole array from the position 1 (we start from 0) and the main idea is that all previous arrays are sorted ascending

# this is STABLE sorting algorithm which means if we encounter that two elements have the same value their order will be preserved

# we also have UNSTABLE sorting algorithms don't guarantee the order will be preserved

def insertionSort(array: List):
    for i in range(1, len(array)):
        j = i - 1
        while array[j] < array[j-1] and j-1 >= 0:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

print(insertionSort([2,3,4,1,6]))