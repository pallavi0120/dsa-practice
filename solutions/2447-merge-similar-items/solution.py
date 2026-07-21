class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort()
        items2.sort()
        i,j=0,0
        res=[]
        while i<len(items1) and j<len(items2):
            id1,value1=items1[i]
            id2,value2=items2[j]
            if id1<id2:
                res.append(items1[i])
                i+=1
            elif id2<id1:
                res.append(items2[j])
                j+=1
            else:
                res.append([id1,value1+value2])
                i+=1
                j+=1
        while i<len(items1):
            res.append(items1[i])
            i+=1
        while j<len(items2):
            res.append(items2[j])
            j+=1
        return res
