#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]
        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # Return if infection found
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # Update the mid value if the infection point not found
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
