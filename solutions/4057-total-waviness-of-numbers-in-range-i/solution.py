class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        w=0
        for i in range(num1,num2+1):
            for j in range(1,len(str(i))-1):
                if int(str(i)[j-1])<int(str(i)[j])>int(str(i)[j+1]) or int(str(i)[j-1])>int(str(i)[j])<int(str(i)[j+1]):
                    w+=1
        return w
