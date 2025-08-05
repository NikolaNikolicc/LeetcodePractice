class Solution {
private:
    vector<vector<int>> perms;
    vector<int> perm;
    
    void helper(vector<int> nums){
        if (nums.size() == 0){
            perms.push_back(perm);
            return;
        }
        for (int i = 0; i < nums.size(); i++){
            perm.push_back(nums[i]);
            int val = nums[i];
            nums.erase(nums.begin() + i);
            helper(nums);
            perm.pop_back();
            nums.insert(nums.begin() + i, val);
        }
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        helper(nums);
        return perms;
    }
};


class SolutionRecursiveNeet {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        if (nums.empty()) {
            return {{}};
        }

        vector<int> tmp = vector<int>(nums.begin() + 1, nums.end());
        vector<vector<int>> perms = permute(tmp);
        vector<vector<int>> res;
        for (const auto& p : perms) {
            for (int i = 0; i <= p.size(); i++) {
                vector<int> p_copy = p;
                p_copy.insert(p_copy.begin() + i, nums[0]);
                res.push_back(p_copy);
            }
        }
        return res;
    }
};

class SolutionIterativeNeet {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> perms = {{}};
        for (int num : nums) {
            vector<vector<int>> new_perms;
            for (const auto& p : perms) {
                for (int i = 0; i <= p.size(); i++) {
                    vector<int> p_copy = p;
                    p_copy.insert(p_copy.begin() + i, num);
                    new_perms.push_back(p_copy);
                }
            }
            perms = new_perms;
        }
        return perms;
    }
};