class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;

        while (l < r){
            int sum = numbers[l] + numbers[r];
            if (sum == target){
                return {l + 1, r + 1};
            } else if (sum < target){
                l++;
            } else {
                r--;
            }
        }

        return {-1, -1};
    }
};
// The code defines a solution to the problem of finding two numbers in a sorted array that add up to a given target.
// It uses a two-pointer technique where one pointer starts at the beginning and the other at the end of the array.
// The function returns the indices of the two numbers that sum to the target, or {-1, -1} if no such pair exists.