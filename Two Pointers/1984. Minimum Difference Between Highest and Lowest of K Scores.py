class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l = 0
        r = k-1
        res = float("inf")
        while r < len(nums):
            res = min(res , abs(nums[l] - nums[r]))
            l = l+1
            r = r+1
        return res