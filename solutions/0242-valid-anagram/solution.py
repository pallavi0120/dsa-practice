'''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(s)
        l2=[]
        for i in l1:
            l2.append()'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*26
        for i in s:
            freq[ord(i)-ord('a')]+=1
        for i in t:
            freq[ord(i)-ord('a')]-=1
        for count in freq:
            if count!=0:
                return False
        return True
