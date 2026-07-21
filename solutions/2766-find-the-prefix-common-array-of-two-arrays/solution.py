class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        res=[0]*n
        cnt=0
        hashmap=[0]*(n+1)
        for i in range(n):
            hashmap[A[i]]+=1
            hashmap[B[i]]+=1
            if A[i]!=B[i]:
                if hashmap[A[i]]==2:
                    cnt+=1
                if hashmap[B[i]]==2:
                    cnt+=1
            else:
                if hashmap[A[i]]==2:
                    cnt+=1
            res[i]=cnt
        return res
