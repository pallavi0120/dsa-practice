class Solution:
    def f(self,i,target,ds,arr,res):
        if i==len(arr):
            if target==0:
                res.append(list(ds))
            return
        if arr[i]<=target:
            ds.append(arr[i])
            self.f(i,target-arr[i],ds,arr,res)
            ds.pop()
        self.f(i+1,target,ds,arr,res)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        ds=[]
        self.f(0,target,ds,candidates,res)
        return res

