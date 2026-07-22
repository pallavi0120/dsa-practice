class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        d1={}
        n=len(score)
        m=len(score[0])
        for i in range(n):
            arr.append(score[i][k])
            d1[score[i][k]]=score[i]
        arr.sort()
        arr.reverse()
        for i in range(n):
            score[i]=d1[arr[i]]
        return score
