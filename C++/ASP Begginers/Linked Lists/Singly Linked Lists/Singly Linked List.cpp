class Node{
    public:
        int val;
        Node* next;

        Node(int v){
            val = v;
            next = nullptr;
        }

        Node(int v, Node* n): val(v), next(n){}
};

class LinkedList {
private: 
    Node* head;
    Node* tail;
public:
    LinkedList() {
        head = new Node(-1);
        tail = head;
    }

    int get(int index) {
        int cnt = -1;
        for(Node* curr = head; curr != nullptr; curr = curr->next){
            if (cnt == index){
                return curr->val;
            }
            cnt++;
        }
        return -1;
    }

    void insertHead(int val) {
        Node* node = new Node(val, head->next);
        head->next = node;
        if(node->next == nullptr){
            tail = node;
        }
    }
    
    void insertTail(int val) {
        tail->next = new Node(val);
        tail = tail->next;
    }

    bool remove(int index) {
        int cnt = -1;
        Node* prev = nullptr;
        for(Node* curr = head; curr != nullptr; curr = curr->next){
            if (cnt == index){
                prev->next = curr->next;
                curr->next = nullptr;
                if (tail == curr){
                    tail = prev;
                }
                return true;
            }
            cnt++;
            prev = curr;
        }
        return false;
    }

    vector<int> getValues() {
        std::vector<int> vec;
        for(Node* curr = head->next; curr != nullptr; curr = curr->next){
            vec.push_back(curr->val);
        }
        return vec;
    }
};
