class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }

        int leftSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            int rightSum = total - leftSum - nums[i];
            if (leftSum == rightSum) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
};
// The code defines a solution to the problem of finding the pivot index in an array.
// The pivot index is the index where the sum of the elements to the left is equal to the sum of the elements to the right.
// The function calculates the total sum of the array, then iterates through it, maintaining a left sum and checking if it equals the right sum at each index.
// If a pivot index is found, it returns that index; otherwise, it returns -1 if no such index exists.