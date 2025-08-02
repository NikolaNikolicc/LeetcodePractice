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
    ListNode* findMiddle(ListNode* head){
        ListNode* fast = head->next, *middle = head;
        while (fast){
            middle = middle->next;
            fast = fast->next;
            if (fast) fast = fast->next;
        }
        return middle;
    }
    
    ListNode* reverseList(ListNode* head){
        ListNode* node = head;
        if (head->next){
            node = reverseList(head->next);
            head->next->next = head;
            head->next = nullptr;
        }
        return node;
    }
    
public:
    int pairSum(ListNode* head) {
        ListNode* middle = findMiddle(head);
        ListNode* first = head;
        ListNode* second = reverseList(middle);

        int maxSum = 0;
        while (first && second){
            maxSum = max(maxSum, first->val + second->val);
            first = first->next;
            second = second->next;
        }
        return maxSum;
    }
};
// The code defines a solution to the problem of finding the maximum twin sum in a linked list.
// It includes functions to find the middle of the list, reverse a linked list, and compute the maximum twin sum. 
// The main function `pairSum` orchestrates these operations to return the desired result.