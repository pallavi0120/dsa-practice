class Solution:
    def helper(self,s, i, num, sign):
        int_min=-2**31 
        int_max=(2**31)-1
        if i>=len(s) or not s[i].isdigit():
            return num*sign
        num=num*10 +int(s[i])
        if sign*num>int_max:
            return int_max
        if num*sign<int_min:
            return int_min
        return self.helper(s,i+1,num,sign)
    def myAtoi(self, s: str) -> int:
        i=0
        while i<len(s) and s[i]==' ':
            i+=1
        sign=1
        c=0
        while i<len(s) and (s[i]=='+' or s[i]=='-'):
            if s[i]=='-':
                sign=-1
                c+=1
            else:
                sign=1
                c+=1
            i+=1
        if c>=2:
            return 0
        return self.helper(s,i,0,sign)
