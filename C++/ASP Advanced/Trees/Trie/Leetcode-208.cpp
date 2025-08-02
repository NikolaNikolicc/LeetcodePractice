class PrefixTree {
    struct PTNode {
        unordered_map<char, PTNode*> umap;
        bool isw = false;
    };
    PTNode* root;
public:
    PrefixTree() {
        root = new PTNode();
    }
    
    void insert(string word) {
        PTNode* curr = root;
        for (char ch: word){
            if (!curr->umap.count(ch)){
                curr->umap[ch] = new PTNode();
            }
            curr = curr->umap[ch];
        }
        curr->isw = true;
    }
    
    bool search(string word) {
        PTNode* curr = root;
        for (char ch: word){
            if (!curr->umap.count(ch)){
                return false;
            }
            curr = curr->umap[ch];
        }
        return curr->isw;
    }
    
    bool startsWith(string prefix) {
        PTNode* curr = root;
        for (char ch: prefix){
            if (!curr->umap.count(ch)){
                return false;
            }
            curr = curr->umap[ch];
        }
        return true;
    }
};
// The code implements a Prefix Tree (Trie) data structure in C++. It provides methods to insert words, search for exact matches, and check if any words start with a given prefix. The Trie is built using nodes that store character mappings and a boolean flag indicating whether a word ends at that node. This structure is efficient for tasks involving word storage and retrieval based on prefixes.