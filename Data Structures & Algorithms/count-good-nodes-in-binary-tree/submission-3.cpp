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
    int count;

    void dfs(TreeNode* node, int Cmax){
        if (node == NULL){
            return;
        }

        if (node->val >= Cmax){
            count++;
            Cmax = node->val;
        }

        dfs(node->left, Cmax);
        dfs(node->right, Cmax);
    }


    int goodNodes(TreeNode* root) {
        count = 0;
        dfs(root, -10001);
        return count;
    }
};