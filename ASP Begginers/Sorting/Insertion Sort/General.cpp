// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        vector<vector<Pair>> res;
        for (int i = 0; i < pairs.size(); i++){
            int j = i - 1;
            while (j > -1 && pairs[j + 1].key < pairs[j].key){
                Pair tmp = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = tmp;
                j--;
            }
            res.push_back(pairs);
        }
        return res;
    }
};
