# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPath(self, root, arr, x):
        if root is None:
            return False

        arr.append(root.val)

        if root.val == x:
            return True

        if self.getPath(root.left, arr, x):
            return True
        if self.getPath(root.right, arr, x):
            return True

        arr.pop()
        return False
    def getPath2(self, root, arr, x,res2):
        if root is None:
            return False

        arr.append(root.val)

        if root.val == x:
            return True

        if self.getPath2(root.left, arr, x,res2):
            res2[0]+='L'
            return True
        if self.getPath2(root.right, arr, x,res2):
            res2[0]+='R'
            return True

        arr.pop()
        return False
    def lca(self, root,p,q):
        if root==None or root.val==p or root.val==q:
            return root
        left=self.lca(root.left,p,q)
        right=self.lca(root.right,p,q)
        if left==None:
            return right
        elif right==None:
            return left
        else:
            return root
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca=self.lca(root,startValue,destValue)
        res1=''
        if lca.val!=startValue:
            arr=[]
            if self.getPath(lca,arr,startValue):
                res1+='U'*(len(arr)-1)
        res2=['']
        if lca.val!=destValue:
            arr=[]
            self.getPath2(lca,arr,destValue,res2)
        return res1+res2[0][::-1]
