class Solution {

    vector<vector<int>> subsets;
    vector<int> subset;
    
public:

    void helper(int pos, vector<int>& nums){
        if (pos == nums.size()){
            subsets.push_back(subset);
            return;
        }
        subset.push_back(nums[pos]);
        helper(pos + 1, nums);
        subset.pop_back();
        while (pos + 1 < nums.size() && nums[pos] == nums[pos + 1])pos++;
        helper(pos + 1, nums);
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        helper(0, nums);
        return subsets;
    }
};
