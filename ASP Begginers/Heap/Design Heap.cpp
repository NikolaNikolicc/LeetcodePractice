class MinHeap {
private:
    vector<int> heap;

    void bubbleUp(int index){
        while (index > 1 && heap[index / 2] > heap[index]){
            swap(heap[index / 2], heap[index]);
            index /= 2;
        }
    }

    void bubbleDown(int index){
        int child = index * 2;
        while (child < heap.size()){ 
            if (child + 1 < heap.size() && heap[child] > heap[child + 1]){
                child += 1;
            }
            if (heap[child] > heap[index]){
                return;
            }

            swap(heap[child], heap[index]);
            index = child;
            child *= 2;
        }
    }

public:
    MinHeap() {heap.push_back(0);} // push dummy value

    void push(int val) {
        heap.push_back(val);
        if(heap.size() > 2)bubbleUp(heap.size() - 1);
    }

    int pop() {
        if (heap.size() == 1){
            return -1;
        }

        if (heap.size() == 2){
            int ret = heap[1];
            heap.pop_back();
            return ret;
        }

        int ret = heap[1];
        heap[1] = heap.back();
        heap.pop_back();
        bubbleDown(1);

        return ret;
    }

    int top() {
        return (heap.size() > 1) ? heap[1] : -1;
    }

    void heapify(const vector<int>& arr) {
        heap.clear();
        heap.push_back(0); // dummy
        heap.insert(heap.end(), arr.begin(), arr.end());
        for (int i = (heap.size() - 1) / 2; i > 0; i--){
            bubbleDown(i);
        }
    }
};
