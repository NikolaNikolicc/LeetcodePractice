from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:
            res = digits[i] + carry
            digits[i] = res % 10
            carry = res // 10

            i -= 1

        if carry:
            digits = [1] + digits

        return digits