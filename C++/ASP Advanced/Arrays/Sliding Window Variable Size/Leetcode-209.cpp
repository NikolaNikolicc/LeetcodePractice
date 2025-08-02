class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int minLen = nums.size() + 1;

        int start = 0, sum = 0;

        for (int i = 0; i < nums.size(); i++){
            sum += nums[i];
            while (sum >= target && i >= start){
                minLen = min(minLen, i - start + 1);
                sum -= nums[start];
                start++;
            }
            
        }

        return (minLen == nums.size() + 1) ? 0 : minLen;
    }
};
// The code defines a solution to the problem of finding the minimum length of a contiguous subarray whose sum is at least a given target.
// It uses a sliding window technique where it expands the window by adding elements from the right and shrinks it from the left when the sum exceeds or meets the target.
// The minimum length of such a subarray is tracked and returned, or 0 if no such subarray exists.