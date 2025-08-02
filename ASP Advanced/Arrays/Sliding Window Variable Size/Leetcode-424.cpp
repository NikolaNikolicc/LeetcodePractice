#include <unordered_map>

using namespace std;

class SolutionMaxFreqOptimized {
    unordered_map<char, int>  umap;
    int maxFreq = 0;
    
public:
    int characterReplacement(string s, int k) {
        
        // guaranteed minimum
        int maxLen = min(static_cast<int>(s.size()), k);
        int size = 0;
        int start = 0;
        for(int i = 0; i < s.size(); i++){
            if (++umap[s[i]] > maxFreq) {
                maxFreq = umap[s[i]];
            }
            size++;

            while (size - maxFreq > k) {
                umap[s[start++]]--;
                size--;
            }
            maxLen = max(maxLen, size);

        }

        return maxLen;
    }
};


class Solution {
    unordered_map<char, int>  umap;

    int searchMax(){
        int maxFreq = 0;
        for(const auto& pair: umap){
            maxFreq = max(maxFreq, pair.second);
        }
        return maxFreq;
    }
    
public:
    int characterReplacement(string s, int k) {
        
        // guaranteed minimum
        int maxLen = min(static_cast<int>(s.size()), k);
        int size = 0;
        int start = 0;
        for(int i = 0; i < s.size(); i++){
            umap[s[i]]++;
            size++;

            while (size - searchMax() > k) {
                umap[s[start++]]--;
                size--;
            }
            maxLen = max(maxLen, size);

        }

        return maxLen;
    }
};
// The code defines a solution to the problem of finding the length of the longest substring that can be formed by replacing at most k characters in a given string.
// It uses a sliding window approach with a hash map to keep track of character frequencies.
// The function iterates through the string, expanding the window by adding characters and checking if the number of characters that need to be replaced exceeds k.
// If it does, it shrinks the window from the start until the condition is satisfied, updating the maximum length found so far. 
// The final result is returned as the length of the longest valid substring.