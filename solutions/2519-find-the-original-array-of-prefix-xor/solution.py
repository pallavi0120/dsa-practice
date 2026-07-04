class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n=len(pref)
        op=[0]*n
        op[0]=pref[0]
        for i in range(1,n):
            op[i]=pref[i-1]^pref[i]
        return op
