class Solution {
public:
    // When we add a new star (*) then we will count how many new subarrays containing this star (*) will be made.
    // We will keep on adding that count with each increment on time 't'.

    // The new subarrays will be the portion where the star(*) was not present earlier.
    // i.e. we need to find some kind of left and right boundary 
    // left and right index where star(*) is not present.
    // we can use sorted array / set / etc here.

    /*
        Say we had: aab*cd 
                    we want to count how many new subarray will be made when we add a star(*) at index 1

                     *) a a b * c d (*
                    -1) 0 1 2 3 4 5 (6
            If we add a new star (*) at index 1.
            Then till -1 to 3 will be the portion were there was not a single star before but now it will have

            First here is logic to find number of subarrays containting the star (*) at index 'i (3 here)':
            When we added 3 in sorted set:
            {-1, 3, 6}
            
            left elements count = ((3) - (-1) - 1) 
            right elemets count = ((6) - (3) - 1) 
            => 
            left elements count = (3) 
            right elements count = (2) 
            => 
            total options = (left count + 1) * (right count + 1) = 4 * 3 = 12
            (when we added 3 only in sorted set before 1)
            aab*
            aab*c
            aab*cd
            ab*
            ab*c
            ab*cd
            b*
            b*c
            b*cd
            *
            *c
            *cd

            When we add index 1 in sorted set:
            {-1, 1, 3, 6}
            (1 - -1 -1), (3 - 1 - 1) => (1), (1) => 2 * 2 = 4

            total options till now = 12 + 4 = 16

            (when we added 1 also)
            these are new subarrays added in count
            a*
            a*b
            *
            *b

            and there still will be previous 12 subarrys, just that the (a) of index 1 will be (*) now.
    
            *ab*
            *ab*c
            *ab*cd
            ab*
            ab*c
            ab*cd
            b*
            b*c
            b*cd
            *
            *c
            *cd
    */
    int minTime(string s, vector<int>& order, int k) {
        int n = s.size();
        set<int> sortedIndices;

        // Insert boundary elements.
        sortedIndices.insert(-1);
        sortedIndices.insert(n);

        long long currentCount = 0;
        for (int t = 0; t < n; ++t) {
            int idx = order[t];
            sortedIndices.insert(idx);
            
            auto it = sortedIndices.find(idx);
            // For current index, find left and right boundary index and count of elements.
            auto left = prev(it), right = next(it);
            long long leftCount = idx - (*left) - 1LL;
            long long rightCount = (*right) - idx - 1LL;

            // New subarrays will be (options in left) * (option in right) of current *.
            // Option is always count + 1, as we have option to choose empty subarray also.
            // Add them in total count.
            currentCount += (leftCount + 1) * (rightCount + 1);

            // Return when target count 'k' is achieved
            if (currentCount >= k) {
                return t;
            }
        }

        // We never achieved target count.
        return -1;
    }
};