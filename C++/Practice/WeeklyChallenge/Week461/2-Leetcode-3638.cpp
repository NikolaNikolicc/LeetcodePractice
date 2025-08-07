class Solution {
public:
    int maxBalancedShipments(vector<int>& weight) {
        int currMax = 0, cnt = 0;

        for (auto w: weight){
            if (currMax == 0 || w >= currMax) currMax = w;
            else {
                currMax = 0;
                cnt++;
            }
        }
        return cnt;
    }
};

class SolutionInTwoLines {
public:
    int maxBalancedShipments(vector<int>& weight) {
        int currMax = 0, cnt = 0;

        for (auto w: weight){
            if (currMax == 0 || w >= currMax) currMax = w;
            else currMax = 0, cnt++;
        }
        return cnt;
    }
};