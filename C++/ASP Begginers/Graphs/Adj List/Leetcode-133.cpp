/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
private:
    unordered_map<Node*, Node*> umap;

    void dfs(Node* root){

        if (!root || umap.count(root)){
            return;
        }

        umap[root] = new Node(root->val);

        for (Node* nei: root->neighbors){
            dfs(nei);
            umap[root]->neighbors.push_back(umap[nei]);
        }
    }

public:
    Node* cloneGraph(Node* node) {
        dfs(node);
        return umap[node];
    }
};