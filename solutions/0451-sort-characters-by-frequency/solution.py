class Solution:
    def frequencySort(self, s: str) -> str:
        freq=[]
        for i in range(26):
            freq.append((0,chr(i+ord('a'))))
        for i in range(26):
            freq.append((0,chr(i+ord('A'))))
        for i in range(10):
            freq.append((0,str(i)))
        for ch in s:
            if 96<ord(ch)<123:
                index=ord(ch)-ord('a')
            elif 64<ord(ch)<91:
                index=ord(ch)-ord('A')+26
            else:
                index=int(ch)+52
            freq[index]=(freq[index][0]+1,ch)
        freq.sort(key=lambda x:(-x[0],x[1]))
        res=""
        for f,ch in freq:
            if f>0:
                res+=(ch*f)
        return res

