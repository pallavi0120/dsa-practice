class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for i in sentences:
            words=i.split(' ')
            if len(words)>maxi:
                maxi=len(words)
        return maxi
