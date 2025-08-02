#include <vector>

using namespace std;

class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        if (arr.size() < 2){
            return arr.size();
        }
        
        int res = 1;
        bool stateBigger = (arr[1] > arr[0]);
        int start = 0;
        for (int curr = 1; curr < arr.size(); curr++){
            if (stateBigger && arr[curr] > arr[curr - 1] || !stateBigger && arr[curr] < arr[curr - 1]){
                stateBigger = !stateBigger;
                res = max(curr - start + 1, res);
            } else if (arr[curr] == arr[curr - 1]) {
                start = curr;
                if (curr + 1 < arr.size()){
                    stateBigger = (arr[curr + 1] > arr[curr]);
                }
            } else {
                // exception
                start = curr - 1;
                stateBigger = (arr[curr - 1] > arr[curr]);
            }
        }
        return res;
    }
};
// The code defines a solution to the problem of finding the maximum size of a turbulent subarray.
// A turbulent subarray is defined as one where the elements alternate between being greater than and less than their neighbors.
// The function iterates through the array, maintaining a state to track whether the last comparison was greater or less than.
// It updates the maximum size of the turbulent subarray whenever a valid condition is met, and resets the start index when necessary.
// The final result is returned as the size of the largest turbulent subarray found.