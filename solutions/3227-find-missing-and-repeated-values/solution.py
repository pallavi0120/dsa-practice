class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        op = []
        l = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                l.append(grid[i][j])
        
        for i in range(len(l)):
            if l.count(l[i]) > 1:
                op.append(l[i])
                break
        
        l0 = []
        for i in range(1, ((len(grid)) ** 2)+1):
            l0.append(i)
        for i in l0:
            if i not in l:
                op.append(i)
        return op



        
