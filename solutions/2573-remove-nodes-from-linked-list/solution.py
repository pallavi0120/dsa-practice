# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        st=[]
        n=len(arr)
        for i in range(n-1,-1,-1):
            if not st:
                st.append(arr[i])
            else:
                if st[-1]<=arr[i]:
                    st.append(arr[i])
        st.reverse()
        temp=head
        i=0
        while i<len(st)-1:
            temp.val=st[i]
            temp=temp.next
            i+=1
        temp.val=st[-1]
        temp.next=None
        return head
