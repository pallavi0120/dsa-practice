# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp=head
        s=''
        while temp:
            s+=str(temp.val)
            temp=temp.next
        ans=0
        for i in range(len(s)):
            ans+=int(s[i])*(2**(len(s)-i-1))
        return ans
