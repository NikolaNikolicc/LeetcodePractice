class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int start = 0;
        int i = 0;
        while (i < nums.size()){
            nums[start++] = nums[i++];
            while (i > 0 && i < nums.size() - 1 && nums[i - 1] == nums[i + 1]){
                i++;
            }
        }
        return start;
    }
};

// The code defines a solution to the problem of removing duplicates from a sorted array.
// It uses a two-pointer technique where one pointer (`start`) keeps track of the position to insert unique elements,
// and the other pointer (`i`) iterates through the array. 
// The function returns the new length of the array after removing duplicates, while modifying the input array in place.