class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'1':[],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        op=[]
        l=[]
        if len(digits)==1:
            return d[digits[0]]
        if digits=='':
            return []
        for i in range(len(digits)):
            l.append(d[digits[i]])
        if len(digits)==2:
            for i in range(len(l)-1):
                for j in range(len(l[i])):
                    for k in range(len(l[i+1])):
                        op.append(l[i][j]+l[i+1][k])
        
            return op
        if len(digits)==3:
            for i in range(len(l)-2):
                for j in range(len(l[i])):
                    for k in range(len(l[i+1])):
                        for m in range(len(l[i+2])):
                            op.append(l[i][j]+l[i+1][k]+l[i+2][m])
        
            return op
        if len(digits)==4:
            for i in range(len(l)-3):
                for w in range(len(l[i])):
                    for x in range(len(l[i+1])):
                        for y in range(len(l[i+2])):
                            for z in range(len(l[i+3])):
                                op.append(l[i][w]+l[i+1][x]+l[i+2][y]+l[i+3][z])
        
            return op








        '''for i in range(len(digits)-1):
            for j in range(len(d[digits[i]])):
                for k in range(len(d[digits[i+1]])):
                    op.append(d[digits[i]][j]+d[digits[i+1]][k])'''
        
        
