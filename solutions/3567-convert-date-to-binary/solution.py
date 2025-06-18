class Solution:
    def convertDateToBinary(self, date: str) -> str:
        res1 = bin(int(date[:4]))[2:]
        res2=bin(int(date[5:7]))[2:]
        res3=bin(int(date[8:10]))[2:]
        return res1+'-'+res2+'-'+res3
