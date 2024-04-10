class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]]+=1
        for j in range(len(t)):
            if t[j] in d:
                d[t[j]] -=1
            else:
                d[t[j]] = 1
        for k , v in d.items():
            if v!=0:
                return False
        return True
        print(d)
        