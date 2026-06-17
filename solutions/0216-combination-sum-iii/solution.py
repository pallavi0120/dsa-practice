class Solution:
    def f(self,summ,used,arr,k,res):
        if summ==0 and len(arr)==k:
            res.append(list(arr))
            return
        if summ<=0 or len(arr)>k:
            return
        for i in range(used,10):
            if i<=summ:
                arr.append(i)
                self.f(summ-i,i+1,arr,k,res)
                arr.pop()
            else:
                break
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr,res=[],[]
        self.f(n,1,arr,k,res)
        return res
