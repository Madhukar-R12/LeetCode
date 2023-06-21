class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        #NeetCode Method
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)

        for c in balloon:
            res = min(res,countText[c]//balloon[c])
        return res

        # Own Implementation
        counter = {}
        for i in text:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i]+=1

        balloon = {}
        bal = "balloon"
        for j in bal:
            if j not in balloon:
                balloon[j] = 1
            else:
                balloon[j]+=1      
        #because the starting result has to be more to get the min value
        #the number of possible balloon count cannot be greater than len(text)
        res = len(text)
        for char in balloon:
            if char not in counter:
                return 0
            res = min(res,counter[char]//balloon[char])
        return res