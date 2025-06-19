class Solution:
    def isValid(self, s: str) -> bool:
        d={']':'[','}':'{',')':'('}
        stack=[]
        top=-1
        for i in s:
            if i in d.values():
                stack.append(i)
                top+=1
            if i in d.keys():
                if stack!=[]:
                    if d[i]==stack[top]:
                        stack.pop()
                        top-=1
                    else:
                        return False
                else:
                    return False
        
        return stack==[]
        
