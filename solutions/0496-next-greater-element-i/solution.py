class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op=[]
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j]>nums1[i]:
                    op.append(nums2[j])
                    break
            if len(op)!=i+1:
                op.append(-1)
        return op
