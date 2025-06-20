# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        temp1=head
        while temp1 and temp1.next:
            temp2=temp1.next
            g=gcd(temp1.val,temp2.val)
            gnode=ListNode(g)
            temp1.next=gnode
            gnode.next=temp2
            temp1=gnode.next
        return head
