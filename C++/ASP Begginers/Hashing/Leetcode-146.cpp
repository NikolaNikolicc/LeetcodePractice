class LRUCache {
private:
    struct Node{
        Node* prev;
        Node* next;
        int val;
        int key;

        Node(int key, int val): key(key), val(val), prev(nullptr), next(nullptr){}
        Node(int k, int v, Node* p, Node* n): key(k), val(v), prev(p), next(n){}
    };

    Node* head;
    Node* tail;

    unordered_map<int, Node*> umap;

    int cap;
    int curr;

    void moveToTheFront(int key){
        Node* tmp = umap[key];

        tmp->prev->next = tmp->next;
        tmp->next->prev = tmp->prev;

        tail->prev->next = tmp;
        tmp->prev = tail->prev;
        tmp->next = tail;
        tail->prev = tmp;
    }

public:
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
        curr = 0;
    }
    
    int get(int key) {
        if (umap.count(key)){
            moveToTheFront(key);
            return umap[key]->val;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (umap.count(key)){
            umap[key]->val = value;
            moveToTheFront(key);
            return;
        }

        Node* node = new Node(key, value, tail->prev, tail);
        tail->prev->next = node;
        tail->prev = node;

        if (curr == cap){
            umap.erase(head->next->key);
            Node* tmp = head->next;
            head->next->next->prev = head;
            head->next = head->next->next;
            curr--;
            delete tmp;
        }
        curr++;
        umap[key] = node;

    }
};
