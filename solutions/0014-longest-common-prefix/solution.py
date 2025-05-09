class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output=""
        mini=[]
        for i in range(len(strs)):
            #for j in range(len(strs[i])):
            mini.append(len(strs[i]))
        mi_n=min(mini)
        for j in range(mi_n):
            count=0
            for i in range(len(strs)-1):
                if strs[i][j]==strs[i+1][j]: 
                    count+=1
                else:
                    return output
            if count==len(strs)-1:
                output+=strs[0][j]
        return output
