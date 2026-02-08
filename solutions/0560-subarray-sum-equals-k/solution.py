class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=dict()
        n=len(nums)
        presum=0
        cnt=0
        dic[0]=1
        for i in range(n):
            presum+=nums[i]
            remove=presum-k
            if remove in dic.keys():
                cnt+=dic[remove]
            
            if presum in dic.keys():
                dic[presum]+=1
            else:
                dic[presum]=1
            
        return cnt
