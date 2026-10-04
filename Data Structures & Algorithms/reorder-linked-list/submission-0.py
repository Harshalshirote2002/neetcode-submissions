# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev=curr
            curr=temp

        head1, head2 = head, prev
        while head2:
            next1, next2 = head1.next, head2.next
            head1.next = head2
            head2.next=next1
            head1, head2 = next1, next2


        