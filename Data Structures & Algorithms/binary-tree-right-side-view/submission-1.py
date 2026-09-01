# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = [root]
        level = 0
        ans = []

        while q:
            for i in range(len(q)):
                node = q.pop(0)

                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)
            ans.append(node.val)
        return ans