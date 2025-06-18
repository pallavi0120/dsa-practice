class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            c1=0
            for j in range(len(words[i])):
                for k in range(len(allowed)):
                    if words[i][j]==allowed[k]:
                        c1+=1
            if c1==len(words[i]):
                c+=1
        return c
