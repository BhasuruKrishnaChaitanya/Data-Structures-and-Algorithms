#https://leetcode.com/problems/find-all-duplicates-in-an-array/
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        lst = []
        for i in nums:
            if i in dic:
                dic[i] += 1
                lst.append(i)
            else:
                dic[i] = 1
        return lst
