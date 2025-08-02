class Solution {
private:
    vector<vector<int>> res;
    vector<int> curr;
public:

    void helper(vector<int>& nums, int pos){
        if (pos == nums.size()){
            res.push_back(curr);
            return;
        }
        helper(nums, pos + 1);
        curr.push_back(nums[pos]);
        helper(nums, pos + 1);
        curr.pop_back();
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        helper(nums, 0);
        return res;
    }
};
