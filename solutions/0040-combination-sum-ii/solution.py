class Solution:
    def f(self, ind, target, arr, res, ds):
        if target==0:
            res.append(list(ds))
            return 
        for i in range(ind,len(arr)):
            if i>ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:
                break
            ds.append(arr[i])
            self.f(i+1,target-arr[i],arr,res,ds)
            ds.pop(-1)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        ds=[]
        candidates.sort()
        self.f(0,target,candidates,res,ds)
        return res
