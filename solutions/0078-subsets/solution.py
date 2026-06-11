class Solution:
    def f(self,i,arr,ds,res):
        #res.append(list(ds))
        if i>=len(arr):
            res.append(list(ds))
            return
        ds.append(arr[i])
        self.f(i+1,arr,ds,res)
        ds.pop()
        self.f(i+1,arr,ds,res)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ds,res=[],[]
        self.f(0,nums,ds,res)
        return res
