class Solution:
    def addDigits(self, num: int) -> int:
        
           
            while len(str(num))>1:
                op=0
                for i in range(len(str(num))):
                    op+=int(str(num)[i])
                num=op
                
            return num
        
