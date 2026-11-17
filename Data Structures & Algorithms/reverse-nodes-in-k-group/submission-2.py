# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        if not head:
            return None
        
        n = k-1
        pointer = head
        list1 = [pointer]
        while n:
            pointer = pointer.next
            if not pointer:
                return head
            list1.append(pointer)
            n-=1

        nextSeries = None
        if pointer:
            nextSeries= pointer.next


        newHead = dummy = list1.pop()
        while list1 and dummy:
            node = list1.pop()
            dummy.next = node
            dummy = dummy.next
        if dummy:
            dummy.next = self.reverseKGroup(nextSeries, k)
        return newHead