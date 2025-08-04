
// optimization: instead of passing cnt as a parameter, we can use combination.size() to determine the count of elements in the current combination
// This reduces the number of parameters in the helper function, making it cleaner and easier to read.
class Solution {
private:
    vector<vector<int>> combinations;
    vector<int> combination;
    
    void helper(int pos, int cnt, int n, int k){
        if (cnt == k){
            combinations.push_back(combination);
            return;
        }
        if (pos == n + 1)return;

        combination.push_back(pos);
        helper(pos + 1, cnt + 1, n, k);
        combination.pop_back();

        helper(pos + 1, cnt, n, k);
    }

public:
    vector<vector<int>> combine(int n, int k) {
        helper(1, 0, n, k);
        return combinations;
    }
};

class SolutionBacktrack2 {
public:
    vector<vector<int>> res;

    vector<vector<int>> combine(int n, int k) {
        res.clear();
        vector<int> comb;
        backtrack(1, n, k, comb);
        return res;
    }

    void backtrack(int start, int n, int k, vector<int>& comb) {
        if (comb.size() == k) {
            res.push_back(comb);
            return;
        }

        for (int i = start; i <= n; i++) {
            comb.push_back(i);
            backtrack(i + 1, n, k, comb);
            comb.pop_back();
        }
    }
};

class SolutionIterative {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> comb(k, 0);
        int i = 0;

        while (i >= 0) {
            comb[i]++;
            if (comb[i] > n) {
                i--;
                continue;
            }

            if (i == k - 1) {
                res.push_back(comb);
            } else {
                i++;
                comb[i] = comb[i - 1];
            }
        }

        return res;
    }
};