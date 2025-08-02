class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int t = 0, d = matrix.size() - 1;
        while (t <= d){
            int m = (t + d) / 2;
            if (matrix[m][0] > target){
                d = m - 1;
            } else if (matrix[m].back() < target){
                t = m + 1;
            } else {
                // start search within column
                int l = 0, r = matrix[0].size() - 1;
                while (l <= r){
                    int middle = (r + l) / 2;
                    if (matrix[m][middle] < target){
                        l = middle + 1;
                    } else if (matrix[m][middle] > target){
                        r = middle - 1;
                    } else{
                        return true;
                    }
                }
                return false; // target not found in this row, but it should be in this row
            }
        }
        return false;
    }
};
