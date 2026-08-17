class Solution:
    def twoSum(self, nums, target):
        n=len(nums)
        dicto={}
        for i in range(0,n):
            diff = target - n
            if diff in dicto:
                return [dicto[diff],i]
            dicto[n]=i


        
        