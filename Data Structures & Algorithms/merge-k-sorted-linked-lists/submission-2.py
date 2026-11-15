# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        minHeap = []
        heapq.heapify(minHeap)

        counter = 0
        for node in lists:
            head = node
            while head:
                heapq.heappush(minHeap, (head.val, counter, head))
                head = head.next
                counter+=1

        if not minHeap:
            return None

        _, _, res = heapq.heappop(minHeap)
        head = res

        while minHeap:
            _, _, minNode = heapq.heappop(minHeap)
            res.next=minNode

            res = res.next

        return head
            
