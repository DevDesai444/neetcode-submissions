# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxh=0
        def dia(root):
            if root is None:
                return 0
            
            leftHeight = dia(root.left)
            rightHeight = dia(root.right)
            self.maxh = max(self.maxh, (leftHeight + rightHeight))

            return (max(leftHeight,rightHeight) + 1)

        dia(root)
        return self.maxh