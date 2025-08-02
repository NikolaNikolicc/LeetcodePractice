class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int elem = 0;
        while (true){
            if (nums[elem] == 0) return elem;
            int tmp = nums[elem];
            nums[elem] = 0;
            elem = tmp;
        }
    }
};
// The code defines a solution to the problem of finding a duplicate number in an array.
// It uses a modified approach where it marks visited elements by setting them to zero, 
// and returns the first element that is already marked as zero, indicating it has been visited before.