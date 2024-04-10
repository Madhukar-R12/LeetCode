class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list("".join(s))
        goal = list("".join(goal))
        if len(s)!=len(goal):
            return False
        for i in range(len(goal)):
            if goal == s:
                return True
            last = goal.pop(-1)
            goal.insert(0,last)
        return False