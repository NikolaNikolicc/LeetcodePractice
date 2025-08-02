class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 0);
        vector<int> right(nums.size() + 1, 1);

        for (int i = nums.size() - 1; i >= 0; i--){
            right[i] = right[i + 1] * nums[i];
        }

        int left = 1;

        for (int i = 0; i < nums.size(); i++){
            res[i] = left * right[i + 1];
            left *= nums[i];
        }

        return res;
    }
};
// The code defines a solution to the problem of finding the product of all elements in an array except for the element at the current index.
// It uses two auxiliary arrays: one to store the cumulative product of elements to the right of each index and another to compute the final result.
// The function iterates through the array twice: first to fill the right products, and then to compute the result using both left and right products.
// The final result is returned as a vector containing the products for each index, excluding the element at that index.