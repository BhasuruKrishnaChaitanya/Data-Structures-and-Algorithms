#https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31,-1,-1):
            ans += (n % 2)*(2**i)
            n = n//2
        return ans
        # print(n)
        # rev = 0
        # for i in range(32): 
        #     rev = rev << 1            
        #     # rev get binary bit from LSB to MSB of n
        #     rev = rev | ( n & 1 )
        #     n = n >> 1
        # return rev
