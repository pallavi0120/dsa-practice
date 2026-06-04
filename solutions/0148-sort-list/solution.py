# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        l.sort()
        temp=head
        i=0
        while temp:
            temp.val=l[i]
            temp=temp.next
            i+=1
        return head'''
class Solution:
    def merge2LL(self,list1,list2):
        dummyNode=ListNode(-1)
        temp=dummyNode
        while list1 and list2:
            if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        if list1:
            temp.next=list1
        else:
            temp.next=list2
        return dummyNode.next
    def findMiddle(self,head):
        if head is None or head.next is None:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle=self.findMiddle(head)

        right=middle.next
        middle.next=None
        left=head

        left=self.sortList(left)
        right=self.sortList(right)

        return self.merge2LL(left,right)
