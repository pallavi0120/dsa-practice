class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=list(haystack)
        n=list(needle)
        for i in range(len(h)-len(n)+1):
            if h[i:i+len(n)]==n:
                return i
        return -1
