// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1, r = n;
        while (l <= r){
            int version = l + (r - l) / 2;
            bool isBad = isBadVersion(version);
    
            if (isBad){
                r = version - 1;
            } else {
                l = version + 1;
            }
        }

        return l;

    }
};