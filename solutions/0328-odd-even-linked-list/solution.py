# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenHead=evenTail=None
        oddHead=oddTail=None
        temp=head
        c=0
        while temp:
            if c%2==1:
                if evenHead:
                    evenTail.next=temp
                    evenTail=temp
                else:
                    evenHead=evenTail=temp
            else:
                if oddHead:
                    oddTail.next=temp
                    oddTail=temp
                else:
                    oddHead=oddTail=temp
            temp=temp.next
            c+=1
        if evenHead is None:
            return oddHead
        if oddHead is None:
            return evenHead
        oddTail.next=evenHead
        evenTail.next=None
        return oddHead
