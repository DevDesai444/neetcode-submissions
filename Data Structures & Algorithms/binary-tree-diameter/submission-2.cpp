/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int dia(TreeNode* node, int& maxh) {
        if (node == NULL) {
            return 0;
        }
        int lh = dia(node->left, maxh);
        int rh = dia(node->right, maxh);
        maxh = max(maxh, lh + rh);
        return max(lh, rh) + 1;
    }

    int diameterOfBinaryTree(TreeNode* root) {
        int maxh = 0;
        dia(root, maxh);
        return maxh;
    }
};