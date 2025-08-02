class Solution {
public:
    void sortColors(vector<int>& nums) {
        std::unordered_map<int, int> umap;

        for (int elem: nums){
            umap[elem]++;
        }
        
        int pos = 0;
        for (int i = 0; i < 3; i++){
            while (umap[i]-- > 0){
                nums[pos++] = i;
            }
        }
    }
};