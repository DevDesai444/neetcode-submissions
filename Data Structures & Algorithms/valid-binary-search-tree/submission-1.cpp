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
    bool check(TreeNode* node, int low, int high){
        if (node== NULL){
            return true;
        }
        if ((low < node->val) && (node->val < high)){
            return (check(node->left, low, node->val) && check(node->right, node->val, high));
        }
        else{ return false;}
    }

    bool isValidBST(TreeNode* root) {
        return check(root,-1000000001, 1000000001);
    }
};
