class Solution:
    def f(self,ind,sum,arr,ds):
        if ind==len(arr):
            xorr=0
            for i in range(len(ds)):
                xorr^=ds[i]
            sum[0]+=xorr
            return 
        ds.append(arr[ind])
        self.f(ind+1,sum,arr,ds)
        ds.pop()
        self.f(ind+1,sum,arr,ds)
    def subsetXORSum(self, nums: List[int]) -> int:
        ds=[]
        sum=[0]
        self.f(0,sum,nums,ds)
        return sum[0]
