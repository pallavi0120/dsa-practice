class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        length=0
        char={}
        for index,right in enumerate(s):
            if right in char and char[right]>=left:
                left=char[right]+1
            length=max(length,index-left+1)
            char[right]=index
        return length
