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
//  */
class Solution {
public:
    vector<int> ans;
    void bsf(TreeNode* node){
        if (node != NULL){
            bsf(node->left);
            ans.push_back(node->val);
            bsf(node->right);
        }
    }
    int kthSmallest(TreeNode* root, int k) {
        bsf(root);
        return ans[k-1];
    }
};
