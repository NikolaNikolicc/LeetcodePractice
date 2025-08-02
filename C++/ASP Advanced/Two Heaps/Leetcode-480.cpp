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
        while (minHeap.size() > maxHeap.size() - balance + 1){
            int tmp = minHeap.top();
            minHeap.pop();
            maxHeap.push(tmp);
            removeFront();
        }

        while (maxHeap.size() > minHeap.size() + balance + 1){
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
            balance++;
            minHeap.pop();
        }

        while (!maxHeap.empty() && maxHeapDel[maxHeap.top()] > 0){
            int tmp = maxHeap.top();
            maxHeapDel[tmp]--;
            balance--;
            maxHeap.pop();
        }
    }

    void printHeaps(){
        cout << "Balance: " << balance;
        cout << "\nMax Heap: ";
        priority_queue<int> tmpMax = maxHeap;
        while (!tmpMax.empty()) {
            cout << tmpMax.top() << " ";
            tmpMax.pop();
        }
        cout << "\nMin Heap: ";
        priority_queue<int, vector<int>, greater<int>> tmpMin = minHeap;
        while (!tmpMin.empty()) {
            cout << tmpMin.top() << " ";
            tmpMin.pop();
        }
        cout << endl <<"------------------------------" << endl;
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
            printHeaps();
            if (i >= k - 1){
                double result;
                if (minHeap.size() == maxHeap.size() - balance){
                    result = ((double)minHeap.top() + (double)maxHeap.top()) / 2.0;
                } else if (minHeap.size() > maxHeap.size() - balance){
                    result = (double)minHeap.top();
                } else result = (double)maxHeap.top();
                res.push_back(result);
            }
        }
        return res;
    }
};

class SolutionNeetcode {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        priority_queue<int> small;
        priority_queue<int, vector<int>, greater<int>> large;
        unordered_map<int, int> d;

        for (int i = 0; i < k; ++i) {
            small.push(nums[i]);
        }
        for (int i = 0; i < k / 2; ++i) {
            large.push(small.top());
            small.pop();
        }

        vector<double> res;
        res.push_back(k & 1 ? small.top() : (large.top() + 0LL + small.top()) / 2.0);
        for (int i = k; i < nums.size(); ++i) {
            d[nums[i - k]]++;
            int balance = small.size() > 0 && nums[i - k] <= small.top() ? -1 : 1;

            if (nums[i] <= small.top()) {
                small.push(nums[i]);
                balance++;
            } else {
                large.push(nums[i]);
                balance--;
            }

            if (balance > 0) {
                large.push(small.top());
                small.pop();
            }
            if (balance < 0) {
                small.push(large.top());
                large.pop();
            }

            while (!small.empty() && d[small.top()] > 0) {
                d[small.top()]--;
                small.pop();
            }

            while (!large.empty() && d[large.top()] > 0) {
                d[large.top()]--;
                large.pop();
            }

            res.push_back(k & 1 ? small.top() : (large.top() + 0LL + small.top()) / 2.0);
        }

        return res;
    }
};


int main(){
    Solution sol;
    vector<int> nums = {9,7,0,3,9,8,6,5,7,6};
    int k = 2;
    vector<double> result = sol.medianSlidingWindow(nums, k);
    cout << "Medians: ";
    // Print the result
    for (double median : result) {
        cout << median << " ";
    }
}