class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, r = 0, m - 1

        target = (m + n) // 2
        even = ((m + n) % 2 == 0)

        while True:
            
            mid = (l + r) // 2
            nmid = target - mid - 2

            mleft = nums1[mid] if mid >= 0 else float("-inf")
            mright = nums1[mid + 1] if mid + 1 < len(nums1) else float("inf")

            nleft = nums2[nmid] if nmid >= 0 else float("-inf")
            nright = nums2[nmid + 1] if nmid + 1 < len(nums2) else float("inf")

            if mleft <= nright and nleft <= mright:
                # even
                if not (m + n) % 2:
                    return (max(mleft, nleft) + min(mright, nright)) / 2
                # odd
                return min(mright, nright)
            elif mleft > nright:
                r = mid - 1
            else:
                l = mid + 1
    