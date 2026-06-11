class Solution:
    def f(self, ind, arr,ds,res):
        res.append(list(ds))
        #if ind==len(arr):
         #  return
        for i in range(ind,len(arr)):
            if i>ind and arr[i]==arr[i-1]:
                continue
            ds.append(arr[i])
            self.f(i+1,arr,ds,res)
            ds.pop()
            #self.f(i+1,arr,ds,res)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ds,res=[],[]
        nums.sort()
        self.f(0,nums,ds,res)
        return res
