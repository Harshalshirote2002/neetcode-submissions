class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -1*stone)

        while max_heap:
            stone1 = -1* heapq.heappop(max_heap)
            if not max_heap:
                return stone1
            stone2 = -1* heapq.heappop(max_heap)
            remainder = abs(stone1-stone2)
            heapq.heappush(max_heap, -1*remainder)

        

