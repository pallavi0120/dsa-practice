class Solution:
    def interpret(self, command: str) -> str:
        res=''
        s=command
        for i in range(len(command)):
            if s[i]=='G':
                res+='G'
            elif s[i]=='(' and s[i+1]==')' and i+1<len(s):
                res+='o'
            elif s[i]=='(' and s[i+1]=='a' and i+1<len(s):
                res+='al'
        return res
