class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}
        for i, n in enumerate(nums):
            if n in prevMap:
                return True 
            prevMap[n] = i
        return False
        # for i in range (len(nums)):
        #     for j in range (i + 1, len(nums)):
        #         if nums[i] == nums[j]: 
        #             return True
        # return False