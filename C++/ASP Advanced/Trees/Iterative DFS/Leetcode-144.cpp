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

    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> s;
        TreeNode* curr = root;
        while (curr || s.size()){
            if (!curr){
                curr = s.top();
                s.pop();
            } 
            res.push_back(curr->val);
            if (curr->right) s.push(curr->right);
            curr = curr->left;
        }
        return res;
    }
};
// The code implements an iterative pre-order traversal of a binary tree using a stack. It starts from the root and explores the left subtree first, pushing nodes onto the stack as it goes deeper. When it reaches a node with no left child, it pops from the stack to visit the right child. This process continues until all nodes are visited, resulting in a vector containing the values of the nodes in pre-order sequence.