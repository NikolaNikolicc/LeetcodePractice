#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        unordered_map<int, int> map;
        for(int student: students){
            map[student]++;
        }
        for(int sandwich: sandwiches){
            if (map[sandwich] == 0) {
                return map[(sandwich + 1) % 2]; // No more students can take this sandwich
            }
            map[sandwich]--;
        }
        return 0; // All sandwiches were taken
    }
};