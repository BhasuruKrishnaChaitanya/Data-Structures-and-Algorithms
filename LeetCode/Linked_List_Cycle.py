#https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashSet = set()
        while head:
            if hashSet.__contains__(head):
                return True
            else:
                hashSet.add(head)
                head = head.next
        return False
