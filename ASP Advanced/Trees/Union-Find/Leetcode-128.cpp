#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// O(n) time and O(n) space solution using Union-Find
class SolutionUnionFind {
private:
    unordered_map<int, int> parent;
    unordered_map<int, int> rank;

    int maxSize = 0;

    int find(int node){
        
        while (parent[node] != node){
            parent[node] = parent[parent[node]];
            node = parent[node];
        }
        return node;
    }

    bool union_(int x, int y){
        int parx = find(x), pary = find(y);
        if (parx == pary)return false;

        if (rank[parx] > rank[pary]){
            parent[pary] = parx;
            rank[parx] += rank[pary];
            maxSize = max(maxSize, rank[parx]);
        } else {
            parent[parx] = pary;
            rank[pary] += rank[parx];
            maxSize = max(maxSize, rank[pary]);
        }
        return true;
    }
    
public:
    int longestConsecutive(vector<int>& nums) {
        // init
        for (int num: nums){
            if (parent.count(num)) continue;
            parent[num] = num;
            rank[num] = 1;
            maxSize = max(maxSize, rank[num]);
            if (parent.count(num - 1)) union_(num - 1, num);
            if (parent.count(num + 1)) union_(num + 1, num);
        }
        return maxSize;
    }
};

// O(n) time and O(n) space solution using a hash set
class SolutionHashSet {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for (int num : numSet) {
            if (numSet.find(num - 1) == numSet.end()) {
                int length = 1;
                while (numSet.find(num + length) != numSet.end()) {
                    length++;
                }
                longest = max(longest, length);
            }
        }
        return longest;
    }
};

// O(n) time and O(n) space solution using a hash map
class SolutionHashMap {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> mp;
        int res = 0;

        for (int num : nums) {
            if (!mp[num]) {
                mp[num] = mp[num - 1] + mp[num + 1] + 1;
                mp[num - mp[num - 1]] = mp[num];
                mp[num + mp[num + 1]] = mp[num];
                res = max(res, mp[num]);
            }
        }
        return res;
    }
};
// The code implements three different approaches to find the length of the longest consecutive sequence in an unsorted array of integers. The first approach uses a Union-Find data structure to efficiently group consecutive numbers, while the second approach utilizes a hash set to track the presence of numbers and count consecutive sequences. The third approach employs a hash map to store the lengths of consecutive sequences, allowing for quick updates and retrievals. Each method has a time complexity of O(n) and space complexity of O(n), making them efficient for this problem.