class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
               
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                return True
        return False
    
        # res = set(nums)
        # if len(nums)==len(res):
        #     return False
        # else:
        #     return True