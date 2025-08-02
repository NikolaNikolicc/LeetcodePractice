class Solution {
private:
    
    
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {

        // const auto& lambda = [](vector<int> a, vector<int> b){
        //     return a[0] > b[0];
        // }
        
        // unordered_map<int, priority_queue<vector<int>, vector<vector<int>>, decltype(lambda)>> helper(lambda);

        // for (const auto& p: people){
        //     helper[p[1]].push_back(p);
        // }

        // Sort people by height (descending) and k (ascending if heights are equal)
        sort(people.begin(), people.end(), [](const vector<int>& a, const vector<int>& b) {
            return (a[0] > b[0]) || (a[0] == b[0] && a[1] < b[1]);
        });

        for (const auto& p: people){
            cout << " [" << p[0] << "," << p[1] << "] ";
        }
        
        vector<vector<int>> result;
        for (const auto& p : people) {
            // Insert at position p[1] (k)
            result.insert(result.begin() + p[1], p);
        }
        
        return result;
    }
};
// The code implements a solution to the "Queue Reconstruction by Height" problem on LeetCode. It sorts the input list of people based on their heights in descending order and, in case of ties, by their k-values in ascending order. Then, it reconstructs the queue by inserting each person at the index specified by their k-value. The final result is a correctly reconstructed queue that satisfies the given conditions.
// The sorting ensures that taller people are placed first, and the insertion respects the number of people in front of each person with a height greater than or equal to theirs.