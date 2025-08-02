class Solution {
public:
    int climbStairs(int n) {
        int one = 1, two = 1;
        for (int i = 1; i < n; i++){
            int tmp = two;
            two = two + one;
            one = tmp;
        }
        return two;
    }
};