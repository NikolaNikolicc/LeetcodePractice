class SegmentTree {
public:
    int n;
    vector<int> tree;

    SegmentTree(int N) {
        n = N;
        while ((n & (n - 1)) != 0) {
            n++;
        }
        tree.resize(2 * n, 0);
    }

    void update(int i, int val) {
        if (val <= tree[n + i]) return;
        tree[n + i] = val;
        for (int j = (n + i) >> 1; j >= 1; j >>= 1) {
            tree[j] = max(tree[j << 1], tree[(j << 1) + 1]);
        }
    }

    int query(int l, int r) {
        l += n;
        r += n + 1;
        int res = 0;
        while (l < r) {
            if (l & 1) {
                res = max(res, tree[l++]);
            }
            if (r & 1) {
                res = max(res, tree[--r]);
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    }
};

class Solution {
public:
    int lengthOfLIS(vector<int>& nums, int k) {
        int maxVal = *max_element(nums.begin(), nums.end());
        SegmentTree ST(maxVal + 1);
        int res = 0;
        for (int& num : nums) {
            int l = max(0, num - k);
            int r = max(0, num - 1);
            int curr = ST.query(l, r) + 1;
            res = max(res, curr);
            ST.update(num, curr);
        }
        return res;
    }
};
// The code implements a solution to the Longest Increasing Subsequence problem with a constraint on the difference between elements. It uses a Segment Tree to efficiently query and update the maximum length of increasing subsequences that can be formed with the given constraints. The `lengthOfLIS` function iterates through the input array, querying the Segment Tree for the maximum length of subsequences that can be extended by the current number, and updates the tree accordingly. The final result is the maximum length found during the iterations.