#include <cstdint>

class Solution {
    
public:

    uint32_t rvrs(int size, uint32_t res){
        if (size <= 1){
            return res;
        }

        int half = size >> 1;
        uint32_t mask = (1u << half) - 1u;
        uint32_t left = res & mask;
        uint32_t right = (res >> half) & mask;

        uint32_t lower = rvrs(half, right);
        uint32_t upper = rvrs(half, left);

        return (upper << half) | lower;
    }

    uint32_t reverseBits(uint32_t n) {
        return rvrs(32, n);
    }
};
