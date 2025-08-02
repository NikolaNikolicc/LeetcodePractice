#include <vector>
#include <iostream>

using std::vector;
using std::cout;
using std::endl;

class TreeNode {
public:
    int val_;
    TreeNode* left_;
    TreeNode* right_;

    TreeNode(int val, TreeNode* left, TreeNode* right) 
        : val_(val), left_(left), right_(right) {}
};

// Time and space: O(n)
void inorder(TreeNode* root) {
    vector<TreeNode*> stack;
    TreeNode* curr = root;

    while (curr || stack.size()) {
        if (curr) {
            stack.push_back(curr);
            curr = curr->left_;
        } else {
            curr = stack.back();
            stack.pop_back();
            cout << curr->val_ << endl;
            curr = curr->right_;
        }
    }
}

// Time and space: O(n)
void preorder(TreeNode* root) {
    vector<TreeNode*> stack;
    TreeNode* curr = root;

    while (curr || stack.size()) {
        if (curr) {
            cout << curr->val_ << endl;
            if (curr->right_) {
                stack.push_back(curr->right_);
            }
            curr = curr->left_;
        } else {
            curr = stack.back();
            stack.pop_back();
        }
    }
}

// Time and space: O(n)
void postorder(TreeNode* root) {
    vector<TreeNode*> stack = {root};
    vector<bool> visit = {false};

    while (stack.size()) {
        TreeNode* curr = stack.back();
        bool visited = visit.back();
        stack.pop_back();
        visit.pop_back();
        if (curr) {
            if (visited) {
                cout << curr->val_ << endl;
            } else {
                stack.push_back(curr);
                visit.push_back(true);
                stack.push_back(curr->right_);
                visit.push_back(false);
                stack.push_back(curr->left_);
                visit.push_back(false);
            }
        }
    }
}
// The code implements iterative depth-first search (DFS) traversals for binary trees: in-order, pre-order, and post-order. Each traversal uses a stack to keep track of nodes, allowing for efficient traversal without recursion. The `inorder`, `preorder`, and `postorder` functions print the values of the nodes in the respective order as they are visited. This approach is useful for traversing large trees where recursion might lead to stack overflow or inefficiency.