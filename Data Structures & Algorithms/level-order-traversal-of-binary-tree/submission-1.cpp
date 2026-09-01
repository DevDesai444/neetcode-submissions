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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL) {
        return {};
        }

        vector<TreeNode*> q;
        q.push_back(root);
        int level = 0;
        vector<vector<int>> ans;

        while (!q.empty()){
            ans.push_back({});
            int size = q.size();
            for (int i=0;i<size;i++){
                TreeNode* node = q[0];
                q.erase(q.begin());
                ans[level].push_back(node->val);

                if (node->left != NULL){
                    q.push_back(node->left);
                }

                if (node->right != NULL){
                    q.push_back(node->right);
                }    
            }
            level ++;
        }
        return ans;
    }
};
