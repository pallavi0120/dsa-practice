class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum=0
        for i in range(len(costs)):
            sum+=costs[i]
            if sum>coins:
                return i
            elif sum==coins:
                return i+1
            else:
                continue
        return len(costs)
