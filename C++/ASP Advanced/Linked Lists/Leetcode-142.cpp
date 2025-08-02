/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {

        if (!head) return nullptr;
        
        ListNode* fast = head->next, * slow = head;

        while (fast && fast != slow){
            fast = fast->next;
            if (fast) fast = fast->next;
            slow = slow->next;
        }
        if (!fast) return nullptr;

        slow = head;
        fast = fast->next;
        while (slow != fast){
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
};
// The code defines a solution to the problem of detecting a cycle in a linked list.
// It uses a two-pointer technique (Floyd's Cycle Detection Algorithm) to find the cycle and return the starting node of the cycle if it exists, or nullptr if there is no cycle. 