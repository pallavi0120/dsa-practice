# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getChildren(self,root,arr):           
        if root.left is None and root.right is None:
            arr.append(root)
        if root.left:
            self.getChildren(root.left,arr)
        if root.right:
            self.getChildren(root.right,arr)
    def dfs(self,root,curr,all):
        if not root:
            return
        curr.append(root.val)
        if not root.left and not root.right:
            all.append(list(curr))
        else:
            self.dfs(root.left,curr,all)
            self.dfs(root.right,curr,all)
        curr.pop()
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        curr,ans=[],[]
        self.dfs(root,curr,ans)
        op=[]
        for i in range(len(ans)):
            strr=''
            strr+=str(ans[i][0])
            for j in range(1,len(ans[i])):
                strr+='->'
                strr+=str(ans[i][j])
            op.append(strr)
        return op
