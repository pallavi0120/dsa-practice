# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head=None
            return head
        c=1
        temp=head
        while temp.next:
            temp.next
            c+=1
        req=n-c
        c=0
        temp=head
        while temp.next:
            if c==req-1:
                temp.next=temp.next.next
                break
            temp=temp.next
            c+=1
        return head'''
'''class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # If list is empty
        if head is None:
            return None

        cnt = 0
        temp = head

        # Count total number of nodes
        while temp:
            cnt += 1
            temp = temp.next

        # If N equals total nodes → delete head
        if cnt == n:
            return head.next

        # Calculate position from start
        res = cnt - n
        temp = head

        # Traverse to the node before target
        while temp:
            res -= 1
            if res == 0:
                break
            temp = temp.next

        # Delete the node
        temp.next = temp.next.next

        return head'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=dummy
        fast=dummy
        for i in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
