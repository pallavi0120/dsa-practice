'''class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            word=s[i:]+s[:i]
            if word==goal:
                return True
        return False'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        double=s+s
        if goal in double:
            return True
        return False

