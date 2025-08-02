#include <vector>

using namespace std;

class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int cnt = 0, sum = 0;
        
        for (int i = 0; i < arr.size(); i++){
            if (i >= k){
                sum -= arr[i - k];
            }
            sum += arr[i];
            if (sum >= threshold * k && i >= k - 1) cnt++;
        }

        return cnt;
    }
};
// The code defines a solution to the problem of counting the number of contiguous subarrays of size k whose average is at least a given threshold.
// It uses a sliding window technique to maintain the sum of the current window of size k.
// The function iterates through the array, updating the sum by adding the new element and removing the oldest element when the window size exceeds k.
// It checks if the average of the current window meets or exceeds the threshold and increments the count accordingly. 
// Finally, it returns the count of such subarrays.