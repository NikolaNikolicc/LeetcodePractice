class Solution {
    unordered_map<char, vector<char>> adj;
    string res = "";
    unordered_set<char> visited;
    unordered_set<char> path;

    // Compare two words and build the graph
    bool compareWords(const string& w1, const string& w2) {
        int len = min(w1.size(), w2.size());
        for (int i = 0; i < len; i++) {
            if (w1[i] != w2[i]) {
                adj[w1[i]].push_back(w2[i]);
                return true;
            }
        }

        // If w2 is prefix of w1 (e.g. "abc", "ab") → invalid
        return w1.size() <= w2.size();
    }

    // Topological sort with cycle detection
    bool topo(char letter) {
        if (path.count(letter)) return false;     // cycle detected
        if (visited.count(letter)) return true;   // already processed

        path.insert(letter);
        for (char nei : adj[letter]) {
            if (!topo(nei)) return false;
        }
        path.erase(letter);
        visited.insert(letter);
        res += letter;
        return true;
    }

public:
    string foreignDictionary(vector<string>& words) {
        unordered_set<char> letters;

        // Build graph edges from adjacent words
        for (int i = 0; i + 1 < words.size(); i++) {
            if (!compareWords(words[i], words[i + 1])) return "";
        }

        // Collect all unique characters
        for (const string& word : words) {
            for (char c : word) {
                letters.insert(c);
            }
        }

        // Perform topological sort
        for (char letter : letters) {
            if (!topo(letter)) return "";
        }

        reverse(res.begin(), res.end());
        return res;
    }
};
