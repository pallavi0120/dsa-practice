# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def extractnum(l):
            temp=l
            s=''
            while temp:
                s+=str(temp.val)
                temp=temp.next
            s=s[::-1]
            return int(s)
        ans=extractnum(l1)+extractnum(l2)
        s=list(str(ans)[::-1])
        op=ListNode(int(s[0]))
        temp=op
        for i in range(1,len(s)):
            temp.next=ListNode(int(s[i]))
            temp=temp.next
        return op'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        temp=dummy
        carry=0
        while l1 or l2 or carry:
            sum_val=0
            if l1:
                sum_val+=l1.val
                l1=l1.next
            if l2:
                sum_val+=l2.val
                l2=l2.next
            sum_val+=carry
            carry=sum_val//10
            temp.next=ListNode(sum_val%10)
            temp=temp.next
        return dummy.next
