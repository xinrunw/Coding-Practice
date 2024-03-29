# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and l2:
            return l2
        elif not l2 and l1:
            return l1
        elif l1 and l2:
            if l1.val > l2.val:
                result = ListNode(l2.val)
                l2 = l2.next
            else:
                result = ListNode(l1.val)
                l1 = l1.next
            result.next = self.mergeTwoLists(l1, l2)
        else:
            return
        return result