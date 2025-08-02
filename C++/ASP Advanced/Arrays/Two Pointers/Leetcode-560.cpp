class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> umap;

        umap[0] = 1;
        int res = 0;
        int csum = 0;
        for (int num: nums){
            csum += num;
            res += umap[csum - k];
            umap[csum]++;
        }
        return res;
    }
};
// The code defines a solution to the problem of finding the number of continuous subarrays that sum to a given value k.
// It uses a hash map to store cumulative sums and their frequencies, allowing for efficient lookup of the number of subarrays that meet the criteria.
// The function iterates through the array, updating the cumulative sum and checking how many times the required sum has been seen before. 
// The result is returned as the total count of such subarrays.