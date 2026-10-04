# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        counter = 0
        dummy = head

        while dummy:
            counter+=1
            dummy=dummy.next
        
        length = counter
        pos = length - n

        dummy = head
        prev = None
        counter = 0

        # print(pos)

        while dummy:
            if counter == pos:
                if not prev:
                    return dummy.next
                else:
                    prev.next = dummy.next
                    break
            counter+=1
            prev=dummy
            dummy=dummy.next
            # print(prev.val, dummy.val)

        return head

