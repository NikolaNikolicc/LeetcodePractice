#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.length() - 1;

        while (l < r) {
            while (l < r && !alphaNum(s[l])) {
                l++;
            }
            while (r > l && !alphaNum(s[r])) {
                r--;
            }
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }
            l++; r--;
        }
        return true;
    }

    bool alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' || 
                c >= 'a' && c <= 'z' || 
                c >= '0' && c <= '9');
    }
};

// The code defines a solution to the problem of checking if a string is a palindrome, ignoring non-alphanumeric characters and case.
// It uses two pointers to traverse the string from both ends, checking if the characters match after converting them to lowercase.
// The function `alphaNum` checks if a character is alphanumeric, and the main function returns true if the string is a palindrome, otherwise false.