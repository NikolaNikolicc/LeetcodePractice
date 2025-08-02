#include <vector>
#include <queue>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:

    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;

    unordered_map<int, int> minHeapDel, maxHeapDel;

    int balance = 0;

    void add(int val){
        maxHeap.push(val);
        if (!minHeap.empty() && maxHeap.top() > minHeap.top()){
            int tmp = maxHeap.top();
            maxHeap.pop();
            minHeap.push(tmp);
        }
        balanceHeaps();
    }

    void balanceHeaps(){
        removeFront();
        while (minHeap.size() > maxHeap.size() + balance + 1){
            int tmp = minHeap.top();
            minHeap.pop();
            maxHeap.push(tmp);
            removeFront();
        }

        while (maxHeap.size() > minHeap.size() - balance + 1){
            int tmp = maxHeap.top();
            maxHeap.pop();
            minHeap.push(tmp);
            removeFront();
        }
    }

    void removeFront(){
        while (!minHeap.empty() && minHeapDel[minHeap.top()] > 0){
            int tmp = minHeap.top();
            minHeapDel[tmp]--;
            minHeap.pop();
        }

        while (!maxHeap.empty() && maxHeapDel[maxHeap.top()] > 0){
            int tmp = maxHeap.top();
            maxHeapDel[tmp]--;
            maxHeap.pop();
        }
    }

    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> res; 
        for (int i = 0; i < nums.size(); i++){
            if (i >= k) {
                int elem = nums[i - k];
                if (maxHeap.size() && elem <= maxHeap.top()) {
                    balance++;
                    maxHeapDel[elem]++;
                } else if (minHeap.size() && elem >= minHeap.top()){
                    balance--;
                    minHeapDel[elem]++;
                }
            }
            add(nums[i]);
            if (i >= k - 1){
                double result;
                if (minHeap.size() == maxHeap.size()){
                    result = (minHeap.top() + maxHeap.top()) / 2.0;
                } else if (minHeap.size() > maxHeap.size()){
                    result = (double)minHeap.top();
                } else result = (double)maxHeap.top();
                res.push_back(result);
            }
        }
        return res;
    }
};


int main(){
    Solution sol;
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> result = sol.medianSlidingWindow(nums, k);
    for (double median : result) {
        cout << median << " ";
    }
}