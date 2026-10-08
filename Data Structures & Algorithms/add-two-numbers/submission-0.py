# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        product = 1
        tot1 = 0
        while l1:
            tot1 += product * l1.val
            product=product * 10
            l1 = l1.next

        product = 1
        tot2 = 0
        while l2:
            tot2 += product * l2.val
            product = product*10
            l2 = l2.next

        

        total = tot1 + tot2
        if total == 0:
            return ListNode(val=0)
        temp = None
        starter = None
        while total:
            if not temp:
                temp=ListNode(val=total % 10)
                starter = temp
            else:
                temp.next = ListNode(val=total%10)
                temp = temp.next

            total = total//10

        return starter