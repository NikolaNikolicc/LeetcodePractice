class TrieNode {
public:
    TrieNode* child[27]; // a-z + '{' (delimiter)
    int idx;

    TrieNode() {
        for (int i = 0; i < 27; i++) {
            child[i] = nullptr;
        }
        idx = -1;
    }
};

class WordFilter {
private:
    TrieNode* root;
    const char delimiter = '{'; // ASCII 'z' + 1

    void insert(string word, int index) {
        TrieNode* curr = root;
        for (char ch : word) {
            int c = (ch == delimiter) ? 26 : (ch - 'a');
            if (!curr->child[c]) {
                curr->child[c] = new TrieNode();
            }
            curr = curr->child[c];
            curr->idx = index; // Update index along the path
        }
    }

    int search(string word) {
        TrieNode* curr = root;
        for (char ch : word) {
            int c = (ch == delimiter) ? 26 : (ch - 'a');
            if (!curr->child[c]) {
                return -1;
            }
            curr = curr->child[c];
        }
        return curr->idx;
    }

public:
    WordFilter(vector<string>& words) {
        root = new TrieNode();
        for (int w = 0; w < words.size(); w++) {
            string word = words[w];
            int n = word.size();
            // Insert all possible suffix + '{' + word combinations
            for (int i = 0; i <= n; i++) {
                string key = word.substr(i, n) + delimiter + word;
                insert(key, w);
            }
        }
    }

    int f(string prefix, string suffix) {
        string key = suffix + delimiter + prefix;
        return search(key);
    }
};
// The code implements a Trie-based solution for the Word Filter problem on LeetCode. It allows efficient searching of words based on their prefixes and suffixes by storing all combinations of suffixes and prefixes in a Trie. The `insert` method adds these combinations to the Trie, while the `search` method retrieves the index of the word that matches the given prefix and suffix. The use of a delimiter ensures that the prefix and suffix are correctly distinguished during searches.