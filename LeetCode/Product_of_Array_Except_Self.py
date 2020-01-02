#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        R = [1]*length
        for i in range(length-2,-1,-1):
            R[i] = R[i+1]*nums[i+1]
        # print(R)
        L = [1]*length
        lst = []
        lst.append(L[0]*R[0])
        for i in range(1,length):
            L[i] = L[i-1]*nums[i-1]
            lst.append(L[i]*R[i])
        # print(L)
        return lst
