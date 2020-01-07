#https://leetcode.com/problems/largest-number/
class Solution(object):
    def largestNumber(self, nums):
        def greater(a, b):
            if a + b > b + a:
                return 1
            return -1
        s = ''.join(sorted([str(num) for num in nums], cmp = greater, reverse = True))
        if s[0] == '0':
            return '0'
        return s
