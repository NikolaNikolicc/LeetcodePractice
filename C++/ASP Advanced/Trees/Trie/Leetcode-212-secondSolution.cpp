class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord;

    TrieNode() : isWord(false) {}

    void addWord(const string& word) {
        TrieNode* cur = this;
        for (char c : word) {
            if (!cur->children.count(c)) {
                cur->children[c] = new TrieNode();
            }
            cur = cur->children[c];
        }
        cur->isWord = true;
    }
};

class Solution {
    unordered_set<string> res;
    vector<vector<bool>> visit;
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            root->addWord(word);
        }

        int ROWS = board.size(), COLS = board[0].size();
        visit.assign(ROWS, vector<bool>(COLS, false));

        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                dfs(board, r, c, root, "");
            }
        }
        return vector<string>(res.begin(), res.end());
    }

private:
    void dfs(vector<vector<char>>& board, int r, int c, TrieNode* node, string word) {
        int ROWS = board.size(), COLS = board[0].size();
        if (r < 0 || c < 0 || r >= ROWS || 
            c >= COLS || visit[r][c] || 
            !node->children.count(board[r][c])) {
            return;
        }

        visit[r][c] = true;
        node = node->children[board[r][c]];
        word += board[r][c];
        if (node->isWord) {
            res.insert(word);
        }

        dfs(board, r + 1, c, node, word);
        dfs(board, r - 1, c, node, word);
        dfs(board, r, c + 1, node, word);
        dfs(board, r, c - 1, node, word);

        visit[r][c] = false;
    }
};
// The code implements a solution to the Word Search II problem on LeetCode using a Trie data structure. It builds a Trie from the list of words and performs a depth-first search (DFS) on the board to find all words that can be formed by adjacent letters. The DFS explores all four directions (up, down, left, right) and marks visited cells to avoid revisiting them. When a word is found, it is added to the result list, and the Trie is updated accordingly. The solution efficiently handles the search and ensures that duplicate words are not counted multiple times.