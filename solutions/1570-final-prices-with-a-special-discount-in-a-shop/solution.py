class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        op=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    op.append(prices[i]-prices[j])
                    break
            if len(op)!=i+1:
                op.append(prices[i])
        return op
