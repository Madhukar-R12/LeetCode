class Solution:
    def reverseWords(self, s: str) -> str:
        store = ""
        s = s.split()
        print(s)
        s = s[::-1]
        print(s)
        return(" ".join(s))