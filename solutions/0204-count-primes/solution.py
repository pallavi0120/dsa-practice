class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        is_prime=[True]*(n)
        is_prime[0]=is_prime[1]=False
        p=2
        while p*p<=n:
            if is_prime[p]:
                for i in range(p*p,n,p):
                    is_prime[i]=False
            p+=1
        c=0
        for i in range(1,n):
            if is_prime[i]:
                c+=1
        return c
