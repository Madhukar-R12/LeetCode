class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        #Optimal Solution
        
        ans = [0]*len(nums)
        even = 0
        odd = 1
        for i in range(len(nums)):
            if nums[i]>0:
                ans[even] = nums[i]
                even+=2
            else:
                ans[odd] = nums[i]
                odd+=2
        return ans
                
        
       # Brute Force Solution 

#         pos = []
#         neg = []
#         for i in range(len(nums)):
#             if nums[i]>=0:
#                 pos.append(nums[i])
#             else:
#                 neg.append(nums[i])
#         count = 0
#         for k,l in zip(pos,neg):
#             nums[2*count] = k
#             nums[2*count+1] = l
#             count+=1
#         return nums
    
    
            