class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        op=[]
        for i in range(len(candies)):
            if extraCandies+candies[i]>=max(candies):
                op.append(True)
            else:
                op.append(False)
        return op
