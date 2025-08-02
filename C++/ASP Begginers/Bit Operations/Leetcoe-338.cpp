#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res;
        int mask = 1;
        for (int i = 0; i <= n; i++){
            if (i == (mask << 1)){
                mask <<= 1;
            }
            
            if (i < 2){
                res.push_back(i);
            } else {
                res.push_back(res[i - mask] + 1);
            }
        }

        return res;
    }
};
