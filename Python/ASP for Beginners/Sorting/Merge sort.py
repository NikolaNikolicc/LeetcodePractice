
# divide and conquer

# time complexity O(n*log(n))

def mergeSort(array, start, end):
    
    if end - start + 1 <= 1:
        return

    middle = (end - start)//2
    mergeSort(array, start, middle)
    mergeSort(array, middle, end)

    l, r = start, middle
    # temporary save arrays so we don't overwrite unused values
    L = array[start:middle]
    R = array[middle:end]

    # we could allocate separate variable instead of start but since we will not use it anymore we can find it new purpose so it can be used as index for rewriting array

    while l < middle and r < end:
        if L[l] <= R[r]:
            array[start] = L[l]
            l += 1
        else:
            array[start] = R[r]
            r += 1
        start += 1

    while l < middle:
        array[start] = L[l]
        l += 1
        start += 1

    while r < end:
        array[start] = R[r]
        r += 1
        start += 1




arr = [2, 3, 4, 1, 6]
print(mergeSort(arr, 0, len(arr)))