class Solution:
    def reverseDegree(self, s: str) -> int:
        summ=0
        for ind,char in enumerate(s): 
            summ+=((ind+1)*(26-(ord(char)-97)))
        return summ
