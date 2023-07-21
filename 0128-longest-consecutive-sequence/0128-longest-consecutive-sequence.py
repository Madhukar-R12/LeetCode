class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for i in numset:
            if i-1 not in numset:
                length = 1
                while i+1 in numset:
                    i+=1
                    length+=1
                longest = max(length,longest)
        return longest

# [100,4,200,1,3,2]
# [0,3,7,2,5,8,4,6,0,1]
# [1,2,0,1]
# [0]
# [0,0]
# []
