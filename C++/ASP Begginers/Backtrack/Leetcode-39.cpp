class Solution {
private:
    vector<vector<int>> combinations;
    vector<int> combination;

public:
    void helper(vector<int>& nums, int target, int pos){
        if (pos == nums.size() || target <= 0){
            if (target == 0)combinations.push_back(combination);
            return;
        }
        
        helper(nums, target, pos + 1);
        combination.push_back(nums[pos]);
        helper(nums, target - nums[pos], pos);
        combination.pop_back();
        
    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        helper(nums, target, 0);
        return combinations;
    }
};
