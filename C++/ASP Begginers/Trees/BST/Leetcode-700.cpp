class Solution {
public:

    bool canEat(int num, vector<int>& piles, int h){
        long long cnt = 0;
        for (int pile: piles){
            cnt += std::ceil(static_cast<double>(pile) / static_cast<double>(num));
        }
        return cnt <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int end = *std::max_element(piles.begin(), piles.end());
        int start = 1;

        while (start <= end){
            int m = start + (end - start) / 2;

            if (canEat(m, piles, h)){
                end = m - 1;
            } else {
                start = m + 1;
            }
        }

        return start;

    }
};