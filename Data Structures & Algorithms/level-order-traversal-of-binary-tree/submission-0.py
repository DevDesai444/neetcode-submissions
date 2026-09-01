# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        ans = []
        level = 0

        while q:
            ans.append([])
            for n in range(len(q)):
                node = q.pop(0)
                ans[level].append(node.val)

                if (node.left != None):
                    q.append(node.left)

                if (node.right != None):
                    q.append(node.right)

            level+=1
        return ans