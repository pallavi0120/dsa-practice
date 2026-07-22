class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res=[]
        for i in words:
            padaalu=i.split(separator)
            for i in padaalu:
                if i!='':
                    res.append(i)
        return res
