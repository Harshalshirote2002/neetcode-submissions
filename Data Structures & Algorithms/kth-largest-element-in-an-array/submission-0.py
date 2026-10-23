class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = []

        heapq.heapify(max_heap)

        for i in nums:
            heapq.heappush(max_heap, -1*i)

        res = None
        while k:
            res = heapq.heappop(max_heap)
            k-=1

        return -res