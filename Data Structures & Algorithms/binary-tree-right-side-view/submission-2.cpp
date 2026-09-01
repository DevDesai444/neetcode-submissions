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
    vector<int> rightSideView(TreeNode* root) {
        if (root == NULL){
            return {};
        }
        vector<int> ans;
        vector<TreeNode*> q;
        q.push_back(root);
        TreeNode* node;
        while (!q.empty()){
            int size = q.size();
            for (int i=0;i<size;i++){
                node = q[0];
                q.erase(q.begin());

                if (node->left != NULL) {
                    q.push_back(node->left);
                }
                if (node->right != NULL) {
                    q.push_back(node->right);
                }
            }
            ans.push_back(node->val);
        }
        return ans;
    }
};