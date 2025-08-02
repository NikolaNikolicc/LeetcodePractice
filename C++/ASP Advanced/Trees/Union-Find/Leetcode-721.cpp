
class Solution {
private:
    unordered_map<string, int> parent;
    unordered_map<int, int> parentGlobal;
    
    void insertInVector(vector<string>& v, string val){
        int i = 1;
        while (i < v.size() && val > v[i])i++;

        if (i < v.size() && v[i] == val) return;
        v.insert(v.begin() + i, val);
    }

    void initialize(int n){
        for (int i = 0; i < n; i++){
            parentGlobal[i] = i;
        }
    }

    int find(int node){
        int curr = node;
        while (parentGlobal[curr] != curr){
            parentGlobal[curr] = parentGlobal[parentGlobal[curr]];
            curr = parentGlobal[curr];
        }
        return curr;
    }

    int union_(int x, int y){
        int parx = find(x), pary = find(y);

        if (parx == pary) return parx;
        else if (parx < pary) {
            parentGlobal[pary] = parx;
            return parx;
        } else {
            parentGlobal[parx] = pary;
            return pary;
        }
    }

public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {

        vector<vector<string>> res;
        initialize(accounts.size());
        
        for (int a = 0; a < accounts.size(); a++){
            vector<string> account = accounts[a];
            for (int i = 1; i < account.size(); i++){
                string email = account[i];
                if (parent.count(email))
                    parent[email] = union_(parent[email], a);
                else
                    parent[email] = a;                
            }
        }

        unordered_map<int, int> map_entry;
        int entry = 0;
        for (const auto& pair: parent){
            string email = pair.first;
            int p = find(pair.second);
            if (!map_entry.count(p)){
                res.push_back(vector<string>(1, accounts[p][0]));
                map_entry[p] = entry++;
            }
            int position = map_entry[p];
            insertInVector(res[position], email);
        }

        return res;
    }
};
// The code implements a solution to merge accounts based on shared email addresses. It uses a Union-Find data structure to group accounts that share emails, ensuring that all emails belonging to the same account are merged into one. The `accountsMerge` function processes the input accounts, finds connected components, and constructs the result with unique emails for each account. The implementation efficiently handles the merging and ensures that the output is sorted as required.
// The `insertInVector` function is used to maintain the sorted order of emails within each account, ensuring that the final output meets the problem's requirements.