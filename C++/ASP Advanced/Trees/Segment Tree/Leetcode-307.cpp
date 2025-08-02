class SegmentTreeIterative {
public:
    int n;
    vector<int> tree;

    SegmentTreeIterative(int N, vector<int>& A) {
        this->n = N;
        while (__builtin_popcount(n) != 1) {
            n++;
        }
        build(N, A);
    }

    void build(int N, vector<int>& A) {
        tree.resize(2 * n);
        for (int i = 0; i < N; i++) {
            tree[n + i] = A[i];
        }
        for (int i = n - 1; i > 0; --i) {
            tree[i] = tree[i << 1] + tree[i << 1 | 1];
        }
    }

    void update(int i, int val) {
        tree[n + i] = val;
        for (int j = (n + i) >> 1; j >= 1; j >>= 1) {
            tree[j] = tree[j << 1] + tree[j << 1 | 1];
        }
    }

    int query(int l, int r) {
        int res = 0;
        for (l += n, r += n + 1; l < r; l >>= 1, r >>= 1) {
            if (l & 1) res += tree[l++];
            if (r & 1) res += tree[--r];
        }
        return res;
    }
};

class NumArray {
    SegmentTreeIterative* segTree;

public:
    NumArray(vector<int>& nums) {
        this->segTree = new SegmentTreeIterative(nums.size(), nums);
    }
    
    void update(int index, int val) {
        this->segTree->update(index, val);
    }
    
    int sumRange(int left, int right) {
        return this->segTree->query(left, right);
    }
};

class SegmentTreeRecursive {
public:
    int n;
    vector<int> tree;

    SegmentTreeRecursive(int N, vector<int>& A) {
        this->n = N;
        while (__builtin_popcount(n) != 1) {
            n++;
        }
        tree.resize(2 * n);
        build(0, 0, n - 1, A);
    }

    void build(int node, int start, int end, vector<int>& A) {
        if (start == end) {
            tree[node] = (start < A.size()) ? A[start] : 0;
        } else {
            int mid = (start + end) / 2;
            build(2 * node + 1, start, mid, A);
            build(2 * node + 2, mid + 1, end, A);
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) {
                update(2 * node + 1, start, mid, idx, val);
            } else {
                update(2 * node + 2, mid + 1, end, idx, val);
            }
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return 0;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        int leftSum = query(2 * node + 1, start, mid, l, r);
        int rightSum = query(2 * node + 2, mid + 1, end, l, r);
        return leftSum + rightSum;
    }

    void update(int idx, int val) {
        update(0, 0, n - 1, idx, val);
    }

    int query(int l, int r) {
        return query(0, 0, n - 1, l, r);
    }
};

class NumArray {
    SegmentTreeRecursive* segTree;

public:
    NumArray(vector<int>& nums) {
        this->segTree = new SegmentTreeRecursive(nums.size(), nums);
    }
    
    void update(int index, int val) {
        this->segTree->update(index, val);
    }
    
    int sumRange(int left, int right) {
        return this->segTree->query(left, right);
    }
};
// The code implements a Segment Tree data structure in C++ for efficient range queries and updates. It provides two implementations: one using an iterative approach and another using recursion. The `NumArray` class utilizes the Segment Tree to perform range sum queries and updates on an array of integers. The Segment Tree allows for logarithmic time complexity for both updates and queries, making it suitable for scenarios where frequent updates and queries are required on a static array.