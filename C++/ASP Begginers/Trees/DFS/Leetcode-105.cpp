#include <vector>
#include <unordered_map>

using namespace std;


  // Definition for a binary tree node.
  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class SolutionSimplified {
public:
    // halfopen [is, ie)
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder, int pre, int is, int ie){
        for(int i = is; i < ie; i++){
            if (inorder[i] == preorder[pre]){
                TreeNode* root = new TreeNode(preorder[pre]);
                // inorder between [is, i) and prepos > pre
                int prepos = pre;
                root->left = helper(preorder, inorder, prepos + 1, is, i);
                prepos = pre + i - is;

                // inorder between (i, ie) and prepos > pre
                root->right = helper(preorder, inorder, prepos + 1, i + 1, ie);

                return root;
            }
        }
        return nullptr;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder, inorder, 0, 0, inorder.size());
    }    
};

class Solution {
public:
    // halfopen [is, ie)
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder, int pre, int is, int ie){
        for(int i = is; i < ie; i++){
            if (inorder[i] == preorder[pre]){
                TreeNode* root = new TreeNode(preorder[pre]);
                // inorder between [is, i) and prepos > pre
                int prepos = pre;
                for (int j = is; j < i; j++){
                    if (prepos + 1 < preorder.size() && preorder[prepos + 1] == inorder[j]){
                        root->left = helper(preorder, inorder, prepos + 1, is, i);
                        prepos = pre + i - is;
                        break;
                    }
                }

                // inorder between (i, ie) and prepos > pre
                for (int j = i + 1; j < ie; j++){
                    if (prepos + 1 < preorder.size() && preorder[prepos + 1] == inorder[j]){
                        root->right = helper(preorder, inorder, prepos + 1, i + 1, ie);
                        break;
                    }
                }
                
                return root;
            }
        }
        return nullptr;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder, inorder, 0, 0, inorder.size());
    }
};