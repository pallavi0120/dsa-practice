class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        r=[]
        m=[]
        for i in range(len(nums)):
            if nums[i]==pivot:
                m.append(nums[i])
            elif nums[i]<pivot:
                l.append(nums[i])
            else:
                r.append(nums[i])
        return l+m+r
        
        '''s = []
        b = []
        for i in nums:
            for j in nums:
                if j > pivot:
                    b.append(j)
                    nums.remove(j)
                if j < pivot:
                    s.append(j)
                    nums.remove(j)
        nums.sort()
        return s + nums + b'''

