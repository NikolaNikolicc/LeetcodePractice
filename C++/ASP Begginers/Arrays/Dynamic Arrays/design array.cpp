class DynamicArray {
private:
    int* arr;
    int cur;
    int size;
public:

    DynamicArray(int capacity) {
        arr = new int[capacity];    
        cur = 0;
        size = capacity;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (cur >= size){
            resize();
        }
        arr[cur++] = n;
    }

    int popback() {
        return arr[--cur];
    }

    void resize() {
        size *= 2;
        int* newArr = new int[size];
        for(int i = 0; i < size; i++){
            newArr[i] = arr[i];
        }
        delete[] arr;
        arr = newArr;
    }

    int getSize() {
        return cur;
    }

    int getCapacity() {
        return size;
    }
};
