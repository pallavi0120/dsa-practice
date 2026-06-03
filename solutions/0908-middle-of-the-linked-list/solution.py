# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head)
            head=head.next
        m=l[len(l)//2]
        return m'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
