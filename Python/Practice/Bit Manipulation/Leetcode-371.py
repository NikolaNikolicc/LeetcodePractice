class Solution:

    def getSum1(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= (1 << i)
        print(bin(res))
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
            
        return res
    
    def getSum2(self, a: int, b: int) -> int:
        num = 1
        carry = 0

        res = 0
        for i in range(32):

            res |= (a & num) ^ (b & num) ^ carry
            
            # carry
            if (a & num and b & num) or (a & num and carry) or (b & num and carry):
                carry = 1
            else:
                carry = 0
            num <<= 1
            if carry:
                carry = num

            # print("res: " + str(res) + " carry: " + str(carry))

        print(bin(res))
        mask = 0xFFFFFFFF
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
            

        return res
    
sol = Solution()
a = -12
b = -8
print(sol.getSum1(a, b))
print(sol.getSum2(a, b))