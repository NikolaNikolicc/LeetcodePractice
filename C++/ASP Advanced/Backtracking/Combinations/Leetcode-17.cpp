class Solution {
private:
    string codes[10] = { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
    vector<string> combinations;
    string combination;

    void helper(int pos, string digits){
        if (pos == 0)combination = "";
        if (pos == digits.size()){
            combinations.push_back(combination);
            return;
        }
        int digit = digits[pos] - '0';
        for (char ch: codes[digit]){
            combination += ch;
            helper(pos + 1, digits);
            combination.pop_back();
        }
    }
public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0)return combinations;
        helper(0, digits);
        return combinations;
    }
};


class SolutionIterative {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> res = {""};
        vector<string> digitToChar = {
            "", "", "abc", "def", "ghi", "jkl",
            "mno", "qprs", "tuv", "wxyz"
        };

        for (char digit : digits) {
            vector<string> tmp;
            for (string &curStr : res) {
                for (char c : digitToChar[digit - '0']) {
                    tmp.push_back(curStr + c);
                }
            }
            res = tmp;
        }
        return res;
    }
};