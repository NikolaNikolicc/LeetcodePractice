class WordDictionary {

    struct PTNode {
        unordered_map<char, PTNode*> umap;
        bool isw = false;
    };
    PTNode* root;

public:
    WordDictionary() {
        root = new PTNode();
    }
    
    void addWord(string word) {
        PTNode* curr = root;
        for (char ch: word){
            if (!curr->umap.count(ch)){
                curr->umap[ch] = new PTNode();
            }
            curr = curr->umap[ch];
        }
        curr->isw = true;        
    }
    
    bool helperSearch(int pos, string word, PTNode* curr){
        for (int i = pos; i < word.size(); i++){
            char ch = word[i];
            if (ch == '.'){
                for (const auto& pair: curr->umap){
                    if (helperSearch(i + 1, word, pair.second)){
                        return true;
                    }
                }
                return false;
            } else if (curr->umap.count(ch)) {
                curr = curr->umap[ch];
            } else {
                return false;
            }
        }
        return curr->isw;
    }

    bool search(string word) {
        return helperSearch(0, word, root);
    }
};
// The code implements a `WordDictionary` class that allows adding words and searching for them, including support for wildcard characters ('.') that can match any single character. The class uses a trie (prefix tree) to efficiently store and search for words, enabling fast lookups and pattern matching.