# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        
        self.maxVal = float('-inf')
        def helper(root):
            if root is None:
                return 0
            Lval = max(0,helper(root.left))
            Rval = max(0,helper(root.right))
            self.maxVal = max(self.maxVal, root.val + Lval + Rval)

            return (max(Lval, Rval) + root.val)
            
        helper(root)
        return self.maxVal