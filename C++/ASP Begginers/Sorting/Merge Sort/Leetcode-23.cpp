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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (!lists.size()){
            return nullptr;
        }
        
        return helper(0, lists.size() - 1, lists);
    }

    // both side inclusive interval
    ListNode* helper(int s, int e, vector<ListNode*>& lists){

        if (s >= e){
            return lists[s];
        }

        int m = (s + e) / 2;

        helper(s, m, lists);
        helper(m + 1, e, lists);

        merge(lists, s, m + 1);

        return lists[s];
    }

    void merge(vector<ListNode*>& lists, int s, int m){
        ListNode* list1 = lists[s];
        ListNode* list2 = lists[m];
        
        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;

        while (list1 && list2){
            if (list1->val <= list2->val){
                curr->next = list1;
                list1 = list1->next;
            }else{
                curr->next = list2;
                list2 = list2->next;
            }
            curr = curr->next;
        }

        if (list1){
            curr->next = list1;
        }

        if (list2){
            curr->next = list2;
        }

        lists[s] = dummy->next;
    }
};
