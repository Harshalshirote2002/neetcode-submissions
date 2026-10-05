# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        ptr = temp = head

        for _ in range(n):
            ptr = ptr.next

        if not ptr:
            return head.next

        while ptr.next:
            temp = temp.next
            ptr = ptr.next

        temp.next = temp.next.next

        return head
        

