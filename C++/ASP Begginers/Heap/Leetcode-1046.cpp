class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;
        for(int stone: stones){
            maxHeap.push(stone);
        }

        while (maxHeap.size() > 1){
            int first = maxHeap.top();
            maxHeap.pop();
            int sec = maxHeap.top();
            maxHeap.pop();
            if (first > sec){
                maxHeap.push(first - sec);
            }
        }

        return maxHeap.empty() ? 0 : maxHeap.top();
    }
};
