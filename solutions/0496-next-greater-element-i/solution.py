class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        op=[]
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j]>nums1[i]:
                    op.append(nums2[j])
                    break
            if len(op)!=i+1:
                op.append(-1)
        return op'''
        hashtable=[None]*(max(nums2)+1)
        st=[]
        n=len(nums2)
        for i in range(len(nums2)-1,-1,-1):
            while st and st[-1]<=nums2[i]:
                st.pop()
            if not st:
                hashtable[nums2[i]]=-1
            else:
                hashtable[nums2[i]]=st[-1]
            st.append(nums2[i])
        op=[]
        for i in nums1:
            op.append(hashtable[i])
        return op
