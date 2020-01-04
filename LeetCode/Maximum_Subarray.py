#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -2147483648
        max_ending_here = 0
        for i in range(0, len(nums)): 
            max_ending_here = max_ending_here + nums[i] 
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
            if max_ending_here < 0: 
                max_ending_here = 0
        return max_so_far 
