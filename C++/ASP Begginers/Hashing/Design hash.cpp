class HashTable {
private:

    struct Node{
        int key;
        int val;
        Node* next;

        Node(int k, int v): key(k), val(v), next(nullptr){}
    };

    int cap;
    int size;
    vector<Node*> umap;
    
    int hash(int index){
        return index % cap;
    }

public:
    HashTable(int capacity): cap(capacity), size(0) {
        umap.resize(cap, nullptr);
    }

    void insert(int key, int value) {
        int pos = hash(key);

        if(!umap[pos]){
            umap[pos] = new Node(key, value);
            if (++size >= cap / 2.0){
                this->resize();
            }
            return;
        }

        Node* node = umap[pos];
        Node* prev = nullptr;
        while (node){
            if (node->key == key){
                node->val = value;
                return;
            }
            prev = node;
            node = node->next;
        }
        prev->next = new Node(key, value);
        if (++size >= cap / 2.0){
            this->resize();
        }
    }

    int get(int key) {
        Node* node = umap[hash(key)];
        while (node){
            if (node->key == key){
                return node->val;
            }
            node = node->next;
        }
        return -1;
    }

    bool remove(int key) {
        int pos = hash(key);
        Node* node = umap[pos];
        Node* prev = nullptr;
        while (node){
            if (node->key == key){
                if (!prev){
                    umap[pos] = node->next;
                } else {
                    prev->next = node->next;
                }
                delete node;
                size--;
                return true;
            }
            prev = node;
            node = node->next;
        }
        // element not found
        return false;
    }

    int getSize() const {
        return size;
    }

    int getCapacity() const {
        return cap;
    }

    void resize() {
        cap *= 2;
        vector<Node*> newUmap(cap, nullptr);
        
        for (Node* elem: umap){
            while (elem){
                int pos = hash(elem->key);
                if(!newUmap[pos]){
                    newUmap[pos] = elem;
                } else {
                    Node* node = newUmap[pos];
                    while (node->next){
                        node = node->next;
                    }
                    node->next = elem;
                }
                Node* tmp = elem;
                elem = elem->next;
                tmp->next = nullptr;
            }
        }
        umap = newUmap;
    }
};
