class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt=0
        ans=0
        for i in s[::-1]:
            if i=='0':
                cnt+=1
            else:
                ans+=cnt
        return ans
