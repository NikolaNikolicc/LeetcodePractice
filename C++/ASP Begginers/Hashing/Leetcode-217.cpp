class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> uset;

        for (int num: nums){
            if (uset.count(num)){
                return true;
            }
            uset.insert(num);
        }
        return false;
    }
};

class Solution1 {
public:
    bool hasDuplicate(vector<int>& nums) {
        return unordered_set<int>(nums.begin(), nums.end()).size() != nums.size();
    }
};