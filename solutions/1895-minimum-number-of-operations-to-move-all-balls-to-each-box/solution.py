class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        op=[]
        l=list(boxes)
        for i in range(len(l)):
            sum=0     
            for j in range(len(l)):
                if l[j]=="1":
                    sum+=abs(i-j)
            op.append(sum)
        return op
