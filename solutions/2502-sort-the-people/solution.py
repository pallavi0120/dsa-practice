class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d1={}
        arr=[]
        for i in range(len(heights)):
            d1[heights[i]]=names[i]
            arr.append(heights[i])
        arr.sort()
        arr.reverse()
        for i in range(len(names)):
            names[i]=d1[arr[i]]
        return names
