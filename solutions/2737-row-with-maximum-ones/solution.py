class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        maxi,ind=0,0
        for i in range(n):
            if mat[i].count(1)>maxi:
                maxi=mat[i].count(1)
                ind=i
        return [ind,maxi]
