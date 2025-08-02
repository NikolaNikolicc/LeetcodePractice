
class SegmentTree:
    def __init__(self, N):
        self.n = 1
        while self.n < N:
            self.n <<= 1
        self.tree = [0] * (2 * self.n)
    
    def update(self, index, value):
        idx = index + self.n
        if self.tree[idx] >= value:
            return
        self.tree[idx] = value
        while idx > 1:
            idx >>= 1
            new_val = max(self.tree[idx << 1], self.tree[(idx << 1) | 1])
            if self.tree[idx] == new_val:
                break
            self.tree[idx] = new_val
    
    def query(self, left, right):
        res = 0
        l = left + self.n
        r = right + self.n + 1
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        print("query: " + str(res))
        return res

class Solution(object):
    def lengthOfLIS(self, nums, k):
        # Collect all relevant values for coordinate compression
        values = set()
        values.add(0)
        for num in nums:
            values.add(num)
            if num - 1 > 0:
                values.add(num - 1)
            if num - k > 0:
                values.add(num - k)
        

        # print(values)
        # Sort and map to indices
        sorted_values = sorted(values)
        index_map = {val: idx for idx, val in enumerate(sorted_values)}
        size = len(sorted_values)
        print(index_map)
        st = SegmentTree(size)
        max_length = 0
        
        print(st.tree)
        for num in nums:
            print(num)
            lower = num - k
            upper = num - 1
            # Convert to compressed indices
            l = index_map[lower] if lower in index_map else 0
            r = index_map[upper] if upper in index_map else 0
            # Find the maximum length in [l, r]
            current = st.query(l, r) + 1
            # Update the current number's position
            pos = index_map[num]
            st.update(pos, current)
            max_length = max(max_length, current)
            print(st.tree)
        
        return max_length
        

sol = Solution()
nums = [4,2,1,4,3,4,5,8,15]
k = 3
sol.lengthOfLIS(nums, k)