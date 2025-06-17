class Solution:
    def defangIPaddr(self, address: str) -> str:
        add=list(address)
        for i in range(len(add)):
            if add[i]=='.':
                add[i]='[.]'
        op=''
        for i in range(len(add)):
            op+=add[i]
        return op
