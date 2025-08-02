/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fast = head->next, * middle = head;

        while (fast){
            middle = middle->next;
            fast = fast->next;
            if (fast)fast = fast->next;
        }

        return middle;    
    }
};
// The code defines a function to find the middle node of a singly-linked list.
// It uses a two-pointer technique where one pointer moves twice as fast as the other to find the middle efficiently.