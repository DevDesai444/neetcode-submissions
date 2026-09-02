# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count =0
        def dfs(node,Cmax):
            if node is None:
                return

            if (node.val >= Cmax):
                self.count+=1
                Cmax = node.val
            
            dfs(node.left, Cmax)
            dfs(node.right, Cmax)
        dfs(root, -10001)
        return self.count