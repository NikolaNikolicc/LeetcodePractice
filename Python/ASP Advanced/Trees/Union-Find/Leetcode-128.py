class Solution:

    def longestConsecutiveHashing(self, nums):
        nums = set(nums)
        maxVal = 0
        for elem in nums:
            if elem - 1 not in nums:
                cpy = elem
                currMax = 1
                while cpy + 1 in nums:
                    currMax += 1
                    cpy += 1
                maxVal = max(maxVal, currMax)
        return maxVal
        
    
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        par = {}
        rank = {elem: 1 for elem in nums}
        
        numsFiltered = set()
        for elem in nums:
            if elem not in par:
                par[elem] = elem
            numsFiltered.add(elem)

        vertices = []
        for elem in numsFiltered:
            if elem + 1 in numsFiltered:
                vertices.append([elem, elem + 1])

        def find(x):
            curr = par[x]
            while curr != par[curr]:
                par[curr] = par[par[curr]]
                curr = par[curr]
            return curr

        def union(x, y):
            par1, par2 = find(x), find(y)

            if par1 == par2:
                return

            if rank[par1] > rank[par2]:
                par[par2] = par1
            elif rank[par1] < rank[par2]:
                par[par1] = par2
            else:
                par[par2] = par1
                rank[par1] += rank[par2]       
                

        for v in vertices:
            union(v[0], v[1])

        mostElements = {elem: 0 for elem in nums}
        for elem in numsFiltered:
            parent = find(elem)
            mostElements[parent] += 1

        return max(mostElements.values())

