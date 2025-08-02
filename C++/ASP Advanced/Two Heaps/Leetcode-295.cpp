class MedianFinder {
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        minHeap.push(num);
        if (!maxHeap.empty() && minHeap.top() < maxHeap.top()){
            int tmp = minHeap.top();
            minHeap.pop();
            maxHeap.push(tmp);
        }

        if (minHeap.size() > maxHeap.size() + 1){
            int tmp = minHeap.top();
            minHeap.pop();
            maxHeap.push(tmp);
        }

        if (maxHeap.size() > minHeap.size() + 1){
            int tmp = maxHeap.top();
            maxHeap.pop();
            minHeap.push(tmp);
        }
    }
    
    double findMedian() {
        if (minHeap.size() == maxHeap.size()){
            return (minHeap.top() + maxHeap.top()) / 2.0;
        } else if (minHeap.size() > maxHeap.size()){
            return (double)minHeap.top();
        } else return (double)maxHeap.top();
    }
};
// The code is complete and does not require any changes. It implements a class `MedianFinder` that maintains two heaps to efficiently find the median of a stream of numbers. The `addNum` method adds a number to the data structure, while the `findMedian` method returns the current median. The implementation ensures that the heaps are balanced, allowing for quick median retrieval.