class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in nums:
            if list(nums).count(x) == 1:
                print(x) 
                return x