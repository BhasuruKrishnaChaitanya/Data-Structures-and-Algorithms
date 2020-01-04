#https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Variables to store maximum and minimum product till ith index.
        minVal = nums[0]
        maxVal = nums[0]
        maxProduct = nums[0]
        for i in range(1, len(nums), 1):
            # When multiplied by -ve number, maxVal becomes minVal and minVal becomes maxVal.
            if (nums[i] < 0):
                temp = maxVal
                maxVal = minVal
                minVal = temp
            # maxVal and minVal stores the product of subarray ending at arr[i].
            maxVal = max(nums[i], maxVal * nums[i])
            minVal = min(nums[i], minVal * nums[i])
            # Max Product of array.
            maxProduct = max(maxProduct, maxVal)
        # Return maximum product found in array. 
        return maxProduct 
