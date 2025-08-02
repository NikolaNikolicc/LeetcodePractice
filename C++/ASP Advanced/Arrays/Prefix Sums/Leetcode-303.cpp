class NumArray {
private:
    vector<int> prefix;

public:
    NumArray(const vector<int>& nums) {
        prefix = vector<int>(nums.size() + 1, 0);
        for (int i = 0; i < nums.size(); i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
    }

    int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
};
// The code defines a class `NumArray` that allows for efficient querying of the sum of elements in a subarray.
// It uses a prefix sum approach to precompute the sums of all subarrays, allowing for O(1) time complexity when querying the sum of any subarray.
// The `sumRange` function calculates the sum of elements in the specified range by using precomputed sums, ensuring that it handles edge cases where the range touches the boundaries of the array.
// This implementation is efficient for multiple queries on the same array.