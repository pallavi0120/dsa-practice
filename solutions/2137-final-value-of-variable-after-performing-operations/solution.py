class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        op=operations
        for i in range(len(op)):
            if op[i]=='--X' or op[i]=='X--':
                X-=1
            if op[i]=='X++' or op[i]=='++X':
                X+=1
        return X
