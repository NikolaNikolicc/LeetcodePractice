class MyListNode{
public:
    int val;
    MyListNode* prev;
    MyListNode* next;
    MyListNode(int val): val(val), next(nullptr), prev(nullptr) {}
    MyListNode(int val, MyListNode* p, MyListNode* n): val(val), next(n), prev(p) {}
};

class MyLinkedList {
private:
    MyListNode* head;
    MyListNode* tail;
public:
    MyLinkedList() {
        head = new MyListNode(-1);
        tail = new MyListNode(-1);

        head->next = tail;
        tail->prev = head;
    }
    
    int get(int index) {
        int cnt = 0;
        for (MyListNode* curr = head->next; curr->next; curr = curr->next){
            if (cnt == index){
                return curr->val;
            }
            cnt++;
        }
        return -1;
    }
    
    void addAtHead(int val) {
        MyListNode* node = new MyListNode(val, head, head->next);
        head->next->prev = node;
        head->next = node;
    }
    
    void addAtTail(int val) {
        MyListNode* node = new MyListNode(val, tail->prev, tail);
        tail->prev->next = node;
        tail->prev = node;
    }
    
    void addAtIndex(int index, int val) {
        int cnt = 0;
        for (MyListNode* curr = head->next; curr->next; curr = curr->next){
            if (cnt == index){
                MyListNode* node = new MyListNode(val, curr->prev, curr);
                curr->prev->next = node;
                curr->prev = node;
                return;
            }
            cnt++;
        }
        if (cnt == index){
            addAtTail(val);
        }
    }
    
    void deleteAtIndex(int index) {
        int cnt = 0;
        for (MyListNode* curr = head->next; curr->next; curr = curr->next){
            if (cnt == index){
                curr->prev->next = curr->next;
                curr->next->prev = curr->prev;
                delete curr;
                return;
            }
            cnt++;
        }
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */