class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=''
        for i in range(len(words)):
            summ=0
            for j in range(len(words[i])):
                summ+=weights[ord(words[i][j])-97]
            res+=chr(122-(summ%26))
        return res
