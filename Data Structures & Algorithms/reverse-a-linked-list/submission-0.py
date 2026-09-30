# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp1 = None
        temp2 = None
        
        if head:
            while head.next:
                temp2 = head.next
                head.next = temp1
                temp1 = head
                head = temp2

            head.next = temp1
            return head
        else:
            return None
