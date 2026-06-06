class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        op=[]
        for i in range(len(order)):
            if order[i] in friends:
                op.append(order[i])
        return op
