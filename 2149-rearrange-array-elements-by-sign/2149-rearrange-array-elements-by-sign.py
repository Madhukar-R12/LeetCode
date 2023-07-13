class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i]>=0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        arr = []
        for k,l in zip(pos,neg):
            arr.append(k)
            arr.append(l)
        return arr