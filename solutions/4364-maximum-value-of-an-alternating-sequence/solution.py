class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        '''seq=[0]*n
        seq[0]=s
        for i in range(1,n):
            if i%2!=0:
                seq[i]=seq[i-1]+m
            else:
                seq[i]=seq[i-1]-1
        return max(seq)'''
        '''
        if (n-1)%2==0:
            i=n//2
            return s+(i*m)-i
        else:
            i=(n//2)'''
        if n==1:
            return s
        i=(n//2)
        return s+(i*m)-(i-1)
