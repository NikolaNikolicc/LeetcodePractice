class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        
        priority_queue<int> heap;

        vector<pair<int, int>> pairs;
        for (int i = 0; i < profits.size(); i++){
            pairs.push_back({profits[i], capital[i]});
        }

        auto cmp = [](pair<int, int> a, pair<int, int> b){return a.second < b.second;}; 

        sort(pairs.begin(), pairs.end(), cmp);

        // for (int i = 0; i < pairs.size(); i++){
        //     cout << "pair: profit(" << pairs[i].first << "), capital(" << pairs[i].second << ")" << endl;
        // }

        int p = 0;
        for (int i = 0; i < k; i++){
            while (p < pairs.size() && w >= pairs[p].second){
                heap.push(pairs[p++].first);
            }
            if (heap.empty()) return w;
            
            int val = heap.top();
            // cout << "val: " << val << endl;
            w += val;
            heap.pop();
        }

        return w;
    }
};