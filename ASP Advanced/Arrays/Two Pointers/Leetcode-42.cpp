class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> left;
        vector<int> right(height.size());

        int mmax = 0;
        for (int i = 0; i < height.size(); i++){
            mmax = max(mmax, height[i]);
            left.push_back(mmax);
        }

        mmax = 0;
        for (int i = height.size() - 1; i >= 0; i--){
            mmax = max(mmax, height[i]);
            right[i] = mmax;
        }

        int area = 0;
        for (int i = 0; i < height.size(); i++){
            area += min(right[i], left[i]) - height[i];
        }
        return area;
    }
};
// The code defines a solution to the problem of trapping rainwater between bars represented by an array of heights.
// It calculates the maximum height to the left and right of each bar, then computes the trapped water by finding the minimum of these two heights minus the height of the current bar.
// The total area of trapped water is returned as the result.