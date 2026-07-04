'''class Solution:
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
        return res'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        subsets=1<<n
        ans=[]
        for num in range(subsets):
            list=[]
            for i in range(n):
                if num&(1<<i):
                    list.append(nums[i])
            ans.append(list)
        return ans
