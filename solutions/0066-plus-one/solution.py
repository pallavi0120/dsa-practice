class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in range(len(digits)):
            s+=str(digits[i])
        op=str(int(s)+1)
        l=[]
        for i in range(len(op)):
            l.append(int(op[i]))
        return l


        
