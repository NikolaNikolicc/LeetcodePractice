class Solution:
    def isHappy(self, n: int) -> bool:
        squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        visited = set()
        def calc(n):
            res = 0

            while n:
                carry = n % 10
                n //= 10

                res += squares[carry]

            return res

        while n != 1 and n not in visited:
            print(n)
            visited.add(n)
            n = calc(n)

        return n == 1
    
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False
    
    def sumOfSquaresLinkedList(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
    
sol = Solution()
sol.isHappy(19)