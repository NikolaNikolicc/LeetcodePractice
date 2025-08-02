#include <vector>

using namespace std;

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int globMax = nums[0], globMin = nums[0];
        int curMax = 0, curMin = 0, total = 0;

        for (int& num : nums) {
            curMax = max(curMax + num, num);
            curMin = min(curMin + num, num);
            total += num;
            globMax = max(globMax, curMax);
            globMin = min(globMin, curMin);
        }

        return globMax > 0 ? max(globMax, total - globMin) : globMax;
    }
};

class SolutionPrefixSums {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n = nums.size();
        vector<int> rightMax(n);
        rightMax[n - 1] = nums[n - 1];
        int suffixSum = nums[n - 1];

        for (int i = n - 2; i >= 0; --i) {
            suffixSum += nums[i];
            rightMax[i] = max(rightMax[i + 1], suffixSum);
        }

        int maxSum = nums[0];
        int curMax = 0;
        int prefixSum = 0;

        for (int i = 0; i < n; ++i) {
            curMax = max(curMax, 0) + nums[i];
            maxSum = max(maxSum, curMax);
            prefixSum += nums[i];
            if (i + 1 < n) {
                maxSum = max(maxSum, prefixSum + rightMax[i + 1]);
            }
        }

        return maxSum;
    }
};
// The code defines a solution to the problem of finding the maximum sum of a circular subarray.
// It uses two approaches: one with Kadane's algorithm to find the maximum subarray sum and another with prefix sums to handle circular cases.
// The first approach iterates through the array, maintaining a current maximum and minimum sum, while the second approach computes suffix maximums to consider circular subarrays.
// The final result is the maximum of the non-circular and circular subarray sums.