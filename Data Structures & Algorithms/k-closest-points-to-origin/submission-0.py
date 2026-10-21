class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        def get_distance(point):
            x, y = point
            return math.sqrt(x**2 + y**2)

        max_heap = []
        heapq.heapify(max_heap)

        for point in points:
            heapq.heappush(max_heap, (get_distance(point), point[0], point[1]))

        result = []

        k_dummy = k

        while k_dummy:
            min_val = heapq.heappop(max_heap)
            result.append([min_val[1], min_val[2]])
            k_dummy-=1



        return result[:k]