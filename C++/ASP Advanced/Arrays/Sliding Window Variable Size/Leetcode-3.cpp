class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen = 0;

        unordered_set<char> uset;
        int start = 0;
        for (int i = 0; i < s.size(); i++){
            while (uset.count(s[i])){
                uset.erase(s[start++]);
            }
            uset.insert(s[i]);
            maxLen = max(maxLen, i - start + 1);
        }

        return maxLen;
    }
};
// The code defines a solution to the problem of finding the length of the longest substring without repeating characters.
// It uses a sliding window technique with a hash set to keep track of characters in the current substring.
// The function iterates through the string, expanding the window by adding characters and shrinking it from the left when a duplicate character is found.
// The maximum length of such substrings is tracked and returned as the result.