class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        sum=0
        s=str(n)
        for i in range(len(s)):
            p*=int(s[i])
            sum+=int(s[i])
        return p-sum
