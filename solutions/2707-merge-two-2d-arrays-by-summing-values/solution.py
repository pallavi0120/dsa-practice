class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        maxi=0
        for i in nums1:
            if i[0]>maxi:
                maxi=i[0]
        for i in nums2:
            if i[0]>maxi:
                maxi=i[0]
        hashmap=[0]*(maxi+1)
        for i in nums1:
            hashmap[i[0]]+=i[1]
        for i in nums2:
            hashmap[i[0]]+=i[1]
        op=[]
        for i in range(1,len(hashmap)):
            if hashmap[i]!=0:
                op.append([i,hashmap[i]])
        return op
