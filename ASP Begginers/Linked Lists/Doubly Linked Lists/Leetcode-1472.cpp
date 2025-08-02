using namespace std;

class Node{
public:
    Node* next;
    Node* prev;
    string url;
    Node(string u, Node* p, Node* n): url(u), prev(p), next(n){}
    Node(string u): url(u), prev(nullptr), next(nullptr){}
};

class BrowserHistory {
private:
    Node* curr;
public:
    BrowserHistory(string homepage) {
        Node* head = new Node("head");
        Node* tail = new Node("tail");
        curr = new Node(homepage, head, tail);
        head->next = curr;
        tail->prev = curr;
    }
    
    void visit(string url) {
        Node* prev = nullptr;
        for(Node* tmp = curr->next; tmp; tmp = tmp->next){
            if (prev){
                delete prev;
            }
            prev = tmp;
        }
        Node* node = new Node(url, curr, prev);
        curr->next = node;
        prev->prev = node;
        curr = node;
    }
    
    string back(int steps) {
        Node* tmp = curr;
        int cnt = 0;
        while(tmp->prev->prev){
            if (cnt == steps){
                break;
            }
            tmp = tmp->prev;
            cnt++;
        }
        curr = tmp;
        return curr->url;
    }
    
    string forward(int steps) {
        Node* tmp = curr;
        int cnt = 0;
        while(tmp->next->next){
            if (cnt == steps){
                break;
            }
            tmp = tmp->next;
            cnt++;
        }
        curr = tmp;
        return curr->url;
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */