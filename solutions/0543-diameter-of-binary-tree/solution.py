# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self,root,maxi):
        if root is None:
            return 0
        lh=self.f(root.left,maxi)
        rh=self.f(root.right,maxi)
        maxi[0]=max(maxi[0],lh+rh)
        return max(lh,rh)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=[0]
        self.f(root,maxi)
        return maxi[0]
