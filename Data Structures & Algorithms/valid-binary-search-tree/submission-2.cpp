class Solution {
public:
    bool check(TreeNode* node, long long low, long long high) {
        if (node == NULL) {
            return true;
        }
        if ((low < node->val) && (node->val < high)) {
            return (check(node->left, low, node->val) && check(node->right, node->val, high));
        }
        else { return false; }
    }

    bool isValidBST(TreeNode* root) {
        return check(root, pow(-2,31)-1, pow(2,31));
    }
};