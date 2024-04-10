class Solution:
    def reverseWords(self, s: str) -> str:
        store = ""
        s = s.split()
        s = s[::-1]
        return(" ".join(s))