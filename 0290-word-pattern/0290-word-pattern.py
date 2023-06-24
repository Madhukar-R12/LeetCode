class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern)!=len(word):
            return False
        CharToWord = {}
        WordToChar = {}
        
        for c,w in zip(pattern,word):
            if c in CharToWord and CharToWord[c]!=w:
                return False
            if w in WordToChar and WordToChar[w]!=c:
                return False
        
            CharToWord[c] = w
            WordToChar[w] = c
            
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # d = {}
        # s = s.split()
        # for i in range(len(s)):
        #     if s[i][0] not in d:
        #         d[s[i][0]] =1
        #     else:
        #         d[s[i][0]]+=1
        # pat = Counter(pattern)
        # print(pat,d)
        # res = sum(d.values()) - sum(pat.values())
        # if res==0 and len(d)==len(pat):
        #     return True
        # else:
        #     return False
            
            
        