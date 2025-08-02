from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        

        # half inclusive
        def divide(s, e):
            if e - s <= 1:
                return

            m = (s + e) // 2

            divide(s, m)
            divide(m, e)

            arr = conq(s, m, e)
            start = s
            for i in range(len(arr)):
                pairs[start + i] = arr[i]

        def conq(s, m, e):
            s1 = s
            s2 = m

            arr = []
            while s1 < m and s2 < e:
                if pairs[s1].key < pairs[s2].key or pairs[s1].key == pairs[s2].key and s1 < s2:
                    arr.append(Pair(pairs[s1].key, pairs[s1].value))
                    s1 += 1
                else:
                    arr.append(Pair(pairs[s2].key, pairs[s2].value))
                    s2 += 1

            while s1 < m:
                arr.append(Pair(pairs[s1].key, pairs[s1].value))
                s1 += 1

            while s2 < e:
                arr.append(Pair(pairs[s2].key, pairs[s2].value))
                s2 += 1                
                
            return arr

        divide(0, len(pairs))
        return pairs

