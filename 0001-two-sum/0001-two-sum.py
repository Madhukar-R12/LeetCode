class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
                    
            
            
            
            
            
            
            
            
            
#         d = {}
#         for i in range(len(nums)):
#             goal = target - nums[i]
#             if goal in d:
#                 return d[goal],i
#             d[nums[i]] = i
        
            
        
        