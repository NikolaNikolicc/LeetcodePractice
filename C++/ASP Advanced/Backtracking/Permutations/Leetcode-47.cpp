class Solution {
private:
    vector<vector<int>> perms;
    unordered_map<int, int> umap;
    vector<int> perm;
    int size;
    void helper(){
        if (perm.size() == size){
            perms.push_back(perm);
            return;
        }
        for (auto &pair: umap){
            if (pair.second > 0){
                pair.second--;
                perm.push_back(pair.first);
                helper();
                perm.pop_back();
                pair.second++;
            }
        }
    }

public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        size = nums.size();
        for (int n: nums){
            umap[n]++;
        }
        helper();
        return perms;
    }
};