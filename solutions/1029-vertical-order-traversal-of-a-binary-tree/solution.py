# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes={}
        ans=[]
        q=deque()
        q.append((root,0,0))
        while q:
            temp,x,y=q.popleft()
            if x not in nodes:
                nodes[x]={}
            if y not in nodes[x]:
                nodes[x][y]=[]
            nodes[x][y].append(temp.val)
            if temp.left:
                q.append((temp.left,x-1,y+1))
            if temp.right:
                q.append((temp.right,x+1,y+1))
        for i in sorted(nodes.keys()):
            col=[]
            for j in sorted(nodes[i].keys()):
                col.extend(sorted(nodes[i][j]))
            ans.append(col)
        return ans
