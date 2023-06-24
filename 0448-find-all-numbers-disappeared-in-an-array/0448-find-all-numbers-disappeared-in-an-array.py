class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for j in range(len(nums)):
            if nums[j] in d:
                d[nums[j]]+=1
            else:
                d[nums[j]] = 1
        print(d)
        cnt = []
        for i in range(1,len(nums)+1):
            if i in d:
                d[i]-=1
            else:
                cnt.append(i)

        
        return cnt
            