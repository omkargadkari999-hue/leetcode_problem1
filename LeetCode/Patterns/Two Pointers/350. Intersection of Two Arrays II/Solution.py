class Solution:
    def intersect(self, nums1, nums2):
        count = {}

        # Count elements in nums1
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        ans = []

        # Check nums2
        for num in nums2:
            if count.get(num, 0) > 0:
                ans.append(num)
                count[num] -= 1

        return ans