# The idea behind quick sort is to improve Merge sort space complexity because we are doing swaps in place and not merging any lists
# Pivot is element which are splitting array in two subproblems (array with elements which are lower and array with elements which are greater than pivot)
# Problem is potential worst time complexity if we are chosing rightmost element for pivot and the given array is already sorted, so in that case time compl is O(n^2), but in regular case time compl is O(nlogn)

# This is UNSTABLE sorting algorithm [7, 3, 7, 4, 5]

# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# pairs=[(3, "cat"), (2, "dog"), (3, "bird")]
# left = 0
# pivot = 3b

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        if not pairs:
            return []
        
        def quick(s, e):

            if s >= e:
                return

            left = s
            pivot = pairs[e]

            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    tmp = pairs[i]
                    pairs[i] = pairs[left]
                    pairs[left] = tmp
                    # pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1

            # pairs[left], pivot = pivot, pairs[left]
            pairs[e] = pairs[left]
            pairs[left] = pivot
            quick(s, left - 1)
            quick(left + 1, e)

        quick(0, len(pairs) - 1)
        return pairs