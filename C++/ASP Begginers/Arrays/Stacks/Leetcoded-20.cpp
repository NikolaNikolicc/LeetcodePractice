class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> umap = {
            {')','('},
            {']','['},
            {'}','{'}
        };
        std::stack<char> stack;
        for (char c: s){
            if (umap.count(c)){
                if(!stack.empty() && stack.top() == umap[c]){
                    stack.pop();
                }else{
                    return false;
                }
            }else{
                stack.push(c);
            }
        }
        return stack.empty();
    }
};
