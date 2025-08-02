class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        firstLowest = [target[0], float("inf"), float("inf")]
        secondLowest = [float("inf"), target[1], float("inf")]
        thirdLowest = [float("inf"), float("inf"), target[2]]

        for triplet in triplets:
            if triplet[0] == target[0]:
                firstLowest[1] = min(triplet[1], firstLowest[1])
                firstLowest[2] = min(triplet[2], firstLowest[2])

            if triplet[1] == target[1]:
                secondLowest[0] = min(triplet[0], secondLowest[0])
                secondLowest[2] = min(triplet[2], secondLowest[2])

            if triplet[2] == target[2]:
                thirdLowest[1] = min(triplet[1], thirdLowest[1])
                thirdLowest[0] = min(triplet[0], thirdLowest[0])
            
        return max(secondLowest[0], thirdLowest[0]) <= target[0] and \
                max(thirdLowest[1], firstLowest[1]) <= target[1] and \
                max(firstLowest[2], secondLowest[2]) <= target[2]

                