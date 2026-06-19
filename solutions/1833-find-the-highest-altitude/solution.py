class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        op=[0]
        sum=0
        maxi=0
        for i in range(len(gain)):
            sum+=gain[i]
            maxi=max(maxi,sum)
        return maxi
