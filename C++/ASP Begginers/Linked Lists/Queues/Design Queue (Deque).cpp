class Node{
public:
    int val;
    Node* next;
    Node* prev;
    Node(int val): val(val), next(nullptr), prev(nullptr){}
    Node(int v, Node* p, Node* n): val(v), next(n), prev(p){}
};

class Deque {
private:
    Node* head;
    Node* tail;
public:
    Deque() {
        head = new Node(-1);
        tail = new Node(-1);
        head->next = tail;
        tail->prev = head;    
    }

    bool isEmpty() {
        return head->next == tail;
    }

    void append(int value) {
        Node* node = new Node(value, tail->prev, tail);
        tail->prev->next = node;
        tail->prev = node;
    }

    void appendleft(int value) {
        Node* node = new Node(value, head, head->next);
        head->next->prev = node;
        head->next = node;
    }

    int pop() {
        if (this->isEmpty()){
            return -1;
        }
        Node* node = tail->prev;
        tail->prev = node->prev;
        node->prev->next = tail;
        return node->val;
    }

    int popleft() {
        if (this->isEmpty()){
            return -1;
        }
        Node* node = head->next;
        head->next = node->next;
        node->next->prev = head;
        return node->val;
    }
};
