class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> uset;

        for (int i = 0; i < nums.size(); i++){
            if (i > k){
                uset.erase(nums[i - k - 1]);
            }
            
            if (uset.count(nums[i])) return true;
            uset.insert(nums[i]);

        }
        return false;
    }
};
// The code defines a solution to the problem of checking if there are two indices in an array such that the values at those indices are equal and the indices are at most k apart.
// It uses a sliding window technique with an unordered set to keep track of the elements in the current window of size k.
// The function iterates through the array, adding elements to the set and checking for duplicates within the specified range.
// If a duplicate is found, it returns true; otherwise, it returns false after checking all elements.