# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        if head is None or head.next is None:
            return head
        newNode=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newNode
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            temp=head.next
            self.reverseLL(head)
            return temp
        k0=1
        temp=head
        while temp:
            if k0==k:
                first=temp.val
            temp=temp.next
            k0+=1
        length=k0-1
        tempo=head
        c=1
        while tempo:
            if c==length-k+1:
                second=tempo.val
                tempo.val=first
                break
            tempo=tempo.next
            c+=1
        tempi=head
        c=1
        while tempi:
            if c==k:
                tempi.val=second
            tempi=tempi.next
            c+=1
        return head
