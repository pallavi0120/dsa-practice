# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        temp=root
        while True:
            if val>=temp.val:
                if temp.right!=None:
                    temp=temp.right
                else:
                    temp.right=TreeNode(val)
                    break
            else:
                if temp.left!=None:
                    temp=temp.left
                else:
                    temp.left=TreeNode(val)
                    break
        return root
