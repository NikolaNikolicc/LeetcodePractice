class MinStack {
private:
    std::stack<int> s;
    std::stack<int> mins;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        s.push(val);
        int v = std::min(val, mins.empty() ? val : mins.top());
        mins.push(v);
    }
    
    void pop() {
        s.pop();
        mins.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return mins.top();
    }
};
