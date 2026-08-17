class Solution:
    def twoSum(self, nums, target):
        n =len(nums)
        dicto={}
        for i in range(0,n):
            diff = target - nums[i]
            if diff in dicto:
                return [dicto[diff],i]
            dicto[n]=i
            return


        
        