'''class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        word=''
        words=[]
        for i in range(n):
            if s[i]!=' ':
                word+=s[i]
            else:
                if word!='':
                    words.append(word)
                    word=''
        if word!='':
            words.append(word)
        words.reverse()
        res=''
        l=len(words)
        for i in range(l-1):
            res+=words[i]
            res+=' '
        res+=words[l-1]
        return res'''
class Solution:
    def reverseWords(self, s: str) -> str:
        res=''
        i=len(s)-1
        while i>=0:
            while i>=0 and s[i]==' ':
                i-=1
            if i<0:
                break
            end=i
            while i>=0 and s[i]!=' ':
                i-=1
            word=s[i+1:end+1]
            if res!='':
                res+=' '
            res+=word
        return res
