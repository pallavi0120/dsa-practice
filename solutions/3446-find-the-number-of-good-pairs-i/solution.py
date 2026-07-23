class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt=0
        for i in nums1:
            if i%k==0:
                for j in nums2:
                    if i%(j*k)==0:
                        cnt+=1
        return cnt
