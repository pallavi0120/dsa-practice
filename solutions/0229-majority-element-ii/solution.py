class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        c1=0
        c2=0
        el1=-(10**(-9))-1
        el2=(10**9)+1
        for i in range(n):
            if c1==0 and nums[i]!=el2:
                c1=1
                el1=nums[i]
            elif c2==0 and nums[i]!=el1:
                c2=1
                el2=nums[i]
            elif nums[i]==el1:
                c1+=1
            elif nums[i]==el2:
                c2+=1
            else:
                c1-=1
                c2-=1
        l=[]
        c1=0
        c2=0
        for i in range(n):
            if nums[i]==el1:
                c1+=1
            if nums[i]==el2:
                c2+=1
        mini=(n//3)+1
        if c1>=mini:
            l.append(el1)
        if c2>=mini:
            l.append(el2)
        l.sort()
        return l
