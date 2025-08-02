#include <vector>
#include <queue>

using namespace std;

class Solution {

    int findStreamMedian(vector<int>& nums, int k) {
        priority_queue<int> maxHeap;
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (int i = 0; i < nums.size(); i++) {
            minHeap.push(nums[i]);
            if (!maxHeap.empty() && minHeap.top() < maxHeap.top()){
                int temp = minHeap.top();
                minHeap.pop();
                maxHeap.push(temp);
            }
            if (maxHeap.size() > minHeap.size() + 1) {
                int temp = maxHeap.top();
                maxHeap.pop();
                minHeap.push(temp);
            }

            if (minHeap.size() > maxHeap.size() + 1) {
                int temp = minHeap.top();
                minHeap.pop();
                maxHeap.push(temp);
            }
        }
        int result;

        if (maxHeap.size() == minHeap.size()) {
            result = (maxHeap.top() + minHeap.top()) / 2.0;
        } else if (maxHeap.size() > minHeap.size()) {
            result = maxHeap.top();
        } else {
            result = minHeap.top();
        }
        return result;
    }
};