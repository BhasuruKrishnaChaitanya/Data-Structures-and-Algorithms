#https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        total = 0
        while (n != 0):
            total += 1
            n &= (n - 1)
        return total
