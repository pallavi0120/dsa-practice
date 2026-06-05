# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findKthNode(self,head,k):
        temp=head
        while temp and k>1:
            k-=1
            temp=temp.next
        return temp
    def reverseLL(self,head):
        if head is None or head.next is None:
            return head
        newNode=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newNode
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prevNode,nextNode=None,None
        while temp:
            kthNode=self.findKthNode(temp,k)
            if not kthNode:
                if prevNode: 
                    prevNode.next=temp
                    break
            nextNode=kthNode.next
            kthNode.next=None
            self.reverseLL(temp)
            if temp==head:
                head=kthNode
            else:
                prevNode.next=kthNode
            prevNode=temp
            temp=nextNode
        return head
