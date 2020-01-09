#https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #Iterative
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        #Recursive
        # if not head or not head.next:
        #     return head
        # head_next = head.next
        # new_head = self.reverseList(head_next)
        # head_next.next = head
        # head.next = None
        # return new_head
