class Solution:
    def reverse(self, x: int) -> int:
        neg = (x < 0)
        if x < 0:
            x *= -1

        mask = 0x7FFFFFFF
        drop = mask % 10
        mask /= 10
        

        final = 0
        while x:
            carry = x % 10
            x //= 10

            if final > mask or (final == mask and carry > drop):
                return 0

            final = (final * 10) + carry

        return final if not neg else -final