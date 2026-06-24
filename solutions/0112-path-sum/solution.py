# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,curr_path,all_paths):
        if not root:
            return
        curr_path.append(root.val)
        if not root.left and not root.right:
            all_paths.append(list(curr_path))
        else:
            self.dfs(root.left,curr_path,all_paths)
            self.dfs(root.right,curr_path,all_paths)
        curr_path.pop()
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr_path,all_paths=[],[]
        self.dfs(root,curr_path,all_paths)
        summ=[]
        for i in range(len(all_paths)):
            summ.append(sum(all_paths[i]))
        if targetSum in summ:
            return True
        return False
