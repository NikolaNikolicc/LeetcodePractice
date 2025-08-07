class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int p = 1;

        while (p < nums.size() && nums[p] > nums[p - 1])p++;
        if (p == 1 || p >= nums.size() - 1 || nums[p] == nums[p - 1]) return false;

        int q = p--;
        while (q < nums.size() - 1 && nums[q] < nums[q - 1])q++;
        if (q == nums.size() || nums[q] == nums[q - 1]) return false;

        int i = q--;
        while (i < nums.size() && nums[i] > nums[i - 1])i++;
        if (i == nums.size()) return true;

        return false;
    }
};