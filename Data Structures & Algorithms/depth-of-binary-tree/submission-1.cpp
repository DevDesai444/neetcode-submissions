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
    int maxH(TreeNode* node){
        if (node == NULL){ return 0;}

        int lh = maxH(node->left);
        int rh = maxH(node->right);

        if (lh>rh) {return lh+1;}
        else{ return rh+1;}
    }

    int maxDepth(TreeNode* root) {
        return maxH(root);
    }
};
