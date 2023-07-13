class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Optimal approach
        max_prof = 0
        min_prof = float("inf")
        for i in range(len(prices)):
            min_prof =min(min_prof,prices[i])
            max_prof = max(max_prof , prices[i] - min_prof)
        return max_prof

        
        #Bruteforce Approach
        # max_prof = 0  
        # for i in range(len(prices)):
        #     curr = 0
        #     for j in range(i+1,len(prices)):
        #         prof = prices[j] - prices[i]
        #         if prof <=0:
        #             continue
        #         else:
        #             max_prof = max(max_prof,prof)
        # return max_prof





