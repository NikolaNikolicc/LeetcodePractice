#include <vector>
class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        int totalSum = nums[0], sum = 0;

        for (int l = 0; l < nums.size(); l++){
            sum += nums[l];
            totalSum = std::max(totalSum, sum);
            if (sum < 0){
                sum = 0;
            } 
        }
        return totalSum;
    }
};
// The code defines a solution to the problem of finding the maximum sum of a contiguous subarray using Kadane's algorithm.
// It iterates through the array, maintaining a current sum and updating the maximum sum found so far.
// If the current sum becomes negative, it is reset to zero, as a negative sum would not contribute to a maximum subarray.