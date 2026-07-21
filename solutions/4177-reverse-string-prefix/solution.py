class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k>len(s):
            k=k%len(s)
        part1=s[:k]
        part2=s[k:]
        part1=part1[::-1]
        return part1+part2
