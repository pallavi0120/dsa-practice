# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        if head is None or head.next is None:
            return head
        newhead=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newhead
    def middle(self,head):
        if head.next.next is None:
            return head.next
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head.next.next is None:
            return head.val+head.next.val
        first=head
        m=self.middle(head)
        last=self.reverseLL(m)
        maxi=0
        while last:
            maxi=max(maxi,first.val+last.val)
            first=first.next
            last=last.next
        return maxi

