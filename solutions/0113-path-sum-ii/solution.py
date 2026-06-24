# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        curr,all=[],[]
        self.dfs(root,curr,all)
        op=[]
        for i in range(len(all)):
            if sum(all[i])==targetSum:
                op.append(all[i])
        return op
