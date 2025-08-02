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
    vector<Pair> quickSort(vector<Pair>& pairs) {
        helper(0, pairs.size() - 1, pairs);
        return pairs;
    }

    // both end inclusive
    void helper(int s, int e, vector<Pair>& pairs){

        if (s >= e){
            return;
        }

        int pivot = e;
        int left = s;

        for(int i = s; i < pivot; i++){
            if (pairs[i].key < pairs[pivot].key){
                std::swap(pairs[left], pairs[i]);
                left++;
            }
        }


        std::swap(pairs[left], pairs[pivot]);

        helper(s, left - 1, pairs);
        helper(left + 1, e, pairs);
        
    }
};
