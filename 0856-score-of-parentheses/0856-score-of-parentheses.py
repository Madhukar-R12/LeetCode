class Solution:
    def scoreOfParentheses(self, s: str):
        bal = 0
        sm=0
        for i in range(len(s)):
            if s[i]=="(":
                bal+=1
            elif s[i]==")":
                bal-=1
                if s[i-1]=='(':
                    sm+= math.pow(2,bal)
                    
        return int(sm)
    
