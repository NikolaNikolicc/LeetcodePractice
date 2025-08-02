
//  Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <stack>

using namespace std;
 
class Solution {
private:
    vector<int> queue;
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<pair<TreeNode*, bool>> s;

        s.push({root, false});
        while (s.size()){
            const auto& pair = s.top();
            s.pop();
            if (!pair.first) continue;
            if (pair.second){
                queue.push_back(pair.first->val);
            } else {
                s.push({pair.first, true});
                s.push({pair.first->right, false});
                s.push({pair.first->left, false});
            }
        }
        return queue;
    }
};
// The code implements an iterative post-order traversal of a binary tree using a stack. It uses a pair to keep track of the current node and whether it has been visited. The traversal visits the left child, then the right child, and finally processes the current node, adding its value to the result vector. This approach avoids recursion and allows for efficient traversal of the tree in post-order fashion.