# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        dummy = temp = ListNode()

        while list1 != None and list2 != None:
            if list1.val > list2.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            
            temp = temp.next

        temp.next = list1 or list2

        return dummy.next

        
