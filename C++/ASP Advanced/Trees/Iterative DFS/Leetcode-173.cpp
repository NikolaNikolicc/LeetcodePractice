
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


#include <stack>

using namespace std;

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
class BSTIterator {
    stack<TreeNode*> s;
public:
    BSTIterator(TreeNode* root) {
        if (!root) return;
        while (root){
            s.push(root);
            root = root->left;
        }
    }
    
    int next() {
        TreeNode* node = s.top();
        s.pop();
        if (node->right){
            TreeNode* curr = node->right;
            while (curr){
                s.push(curr);
                curr = curr->left;
            }
        }
        return node->val;
    }
    
    bool hasNext() {
        return !s.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
// The code implements a binary search tree (BST) iterator using an iterative approach with a stack. The `BSTIterator` class initializes with the root of the BST and pushes all left children onto the stack. The `next` method pops the top node from the stack, pushes its right child and all its left children onto the stack, and returns the value of the popped node. The `hasNext` method checks if there are any nodes left in the stack to iterate over. This implementation allows for efficient in-order traversal of the BST without using recursion.
// The iterator provides a way to traverse the BST in sorted order, making it useful for problems that require sequential access to the elements of the tree.