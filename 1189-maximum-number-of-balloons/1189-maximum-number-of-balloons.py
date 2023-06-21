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
















        # balloon = ['b','a','l','l','o','o','n']
        # d = {}
        # for i in text:
        #     if i in balloon:
        #         if i in d:
        #             d[i]+=1
        #         else:
        #             d[i] = 1
        # print(d)
        # l = []
        # for k,v in d.items():
        #     l.append(v)
        # print(l)
        # count = list(set(l))
        # if len(count)==2:
        #     return sum(l)//7
        # else:
        #     return 0
             
    


        
            
                
        