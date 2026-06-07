# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def snd(self,temp):
        k=2
        while temp and k>1:
            k-=1
            temp=temp.next
        return temp
    def reverseLL(self,head):
        if head is None or head.next is None:
            return head
        newHead=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newHead
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp=head
        prevNode,nextNode=None,None
        while temp:
            snd=self.snd(temp)
            if not snd:
                if prevNode:
                    prevNode.next=temp
                    break
            nextNode=snd.next
            snd.next=None
            self.reverseLL(temp)
            if head==temp:
                head=snd
            else:
                prevNode.next=snd
            prevNode=temp
            temp=nextNode
        return head
