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
    bool hasCycle(ListNode* head) {
        ListNode* fast = head->next, * slow = head;

        while (fast && fast != slow){
            fast = fast->next;
            if (fast) fast = fast->next;
            slow = slow->next;
        }
        return (!fast)? false : true;
    }
};
// The code defines a solution to the problem of detecting a cycle in a linked list.
// It uses a two-pointer technique (Floyd's Cycle Detection Algorithm) to determine if a cycle exists in the list.
// The function returns true if a cycle is detected, otherwise it returns false.