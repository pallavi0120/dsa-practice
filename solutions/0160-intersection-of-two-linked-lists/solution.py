# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headB:
            temp=headA
            while temp:
                if temp==headB:
                    return headB
                temp=temp.next
            headB=headB.next
        return None'''
'''class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        temp=headA
        while temp:
            s.add(temp)
            temp=temp.next
        tempo=headB
        while tempo:
            if tempo in s:
                return tempo
            tempo=tempo.next
        return None'''
''''class Solution:
    def getDifference(self,head1,head2):
        len1,len2=0,0
        while head1 or head2:
            if head1:
                len1+=1
                head1=head1.next
            if head2:
                len2+=1
                head2=head2.next
        return len1-len2
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        diff=self.getDifference(headA,headB)
        if diff<0:
            while diff !=0: 
                headB=headB.next
                diff+=1
        else:
            while diff!=0:
                headA=headA.next
                diff-=1
        while headA:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1=headA
        d2=headB
        while d1!=d2:
            if d1:
                d1=d1.next
            else:
                d1=headB
            if d2:
                d2=d2.next
            else:
                d2=headA
            if d1==None and d2==None:
                return None
        return d1
