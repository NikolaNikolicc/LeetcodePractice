class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;

        int maxa = 0;
        while (l < r){
            int a = (r - l) * min(heights[r], heights[l]);
            maxa = max(maxa, a);
            if (heights[l] < heights[r]){
                l++;
            } else {
                r--;
            }

        }

        return maxa;
    }
};
// The code defines a solution to the problem of finding the maximum area of water that can be contained between two vertical lines represented by an array of heights.