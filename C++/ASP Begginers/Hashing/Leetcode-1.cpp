class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        for(int i = 0; i < nums.size(); i++){
            int num = nums[i];
            if (umap.count(target - num)){
                return {umap[target - num], i};
            }

            umap[num] = i;
        }
    }
};
