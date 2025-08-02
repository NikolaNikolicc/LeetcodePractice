class Solution(object):
    def permute(self, nums):
        permutations = [[]]

        for n in nums:
            newPermutations = []
            for permutation in permutations:
                for i in range(len(permutation) + 1):
                    per = permutation[:i] + [n] + permutation[i:]
                    newPermutations.append(per)

            permutations = newPermutations

        return permutations