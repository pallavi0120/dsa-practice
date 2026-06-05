# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        temp=head
        length=1
        while temp.next:
            length+=1
            temp=temp.next
        temp.next=head
        k=k%length
        cut=length-k
        tempo=head
        for _ in range(cut-1):
            tempo=tempo.next
        newHead=tempo.next
        tempo.next=None
        return newHead
