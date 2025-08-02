class NumMatrix {
    vector<vector<int>> sums;
public:
    NumMatrix(vector<vector<int>>& matrix) {
        sums = vector<vector<int>>(matrix.size(), vector<int>(matrix[0].size(), 0));
        for (int r = 0; r < matrix.size(); r++){
            int s = 0;
            for (int c = 0; c < matrix[0].size(); c++){
                s += matrix[r][c];
                sums[r][c] = s + sums[max(0, r - 1)][c];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int left = (col1 > 0) ? sums[row2][col1 - 1] : 0;
        int upper = (row1 > 0) ? sums[row1 - 1][col2] : 0;
        int upperleft = (row1 == 0 || col1 == 0) ? 0 : sums[row1 - 1][col1 - 1];

        return sums[row2][col2] - left - upper + upperleft;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
// The code defines a class `NumMatrix` that allows for efficient querying of the sum of elements in a submatrix.
// It uses a prefix sum approach to precompute the sums of all submatrices, allowing for O(1) time complexity when querying the sum of any rectangular region in the matrix.
// The `sumRegion` function calculates the sum of elements in the specified region by using precomputed sums, ensuring that it handles edge cases where the region touches the boundaries of the matrix. 
// This implementation is efficient for multiple queries on the same matrix.