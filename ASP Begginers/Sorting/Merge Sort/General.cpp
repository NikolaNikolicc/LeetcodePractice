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
    vector<Pair> mergeSort(vector<Pair>& pairs) {
        helper(0, pairs.size() -1, pairs);
        return pairs;
    }

    // inclusive interval left and right
    void helper(int s, int e, vector<Pair>& pairs){
        if (e <= s){
            return;
        }
        
        int m = (s + e) / 2;

        helper(s, m, pairs);
        helper(m + 1, e, pairs);

        merge(s, m, e, pairs);

    }

    void merge(int s, int m, int e, vector<Pair>& pairs){
        vector<Pair> L(pairs.begin() + s, pairs.begin() + m + 1); // halfopen interval
        vector<Pair> R(pairs.begin() + m + 1, pairs.begin() + e + 1); // halfopen interval
        
        int left = 0, right = 0, combined = s;

        while (left < L.size() && right < R.size()){
            if(L[left].key <= R[right].key){
                pairs[combined] = L[left++];
            }else{
                pairs[combined] = R[right++];
            }
            combined++;
        }

        while (left < L.size()){
            pairs[combined++] = L[left++];
        }

        while (right < R.size()){
            pairs[combined++] = R[right++];
        }
    }
};
