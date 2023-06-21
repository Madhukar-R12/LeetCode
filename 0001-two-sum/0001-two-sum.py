class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(0,n):
            goal = target - nums[i]
            if(goal in m):
                return [m[goal], i]
            m[nums[i]] = i







        
        # for i in range(len(nums)):
        #     res = nums[i]
        #     for j in range(i+1,len(nums)):
        #         ser = nums[j]
        #         if nums[i]+nums[j] == target:
        #             return(i,j)
        
        