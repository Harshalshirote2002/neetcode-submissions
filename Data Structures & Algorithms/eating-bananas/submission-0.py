class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def canFinish(k:int) -> bool:
            hours = 0
            for item in piles:
                hours += item//k
                if item % k!=0:
                    hours +=1
                if hours>h:
                    return False

            return True
        
        if len(piles) == h:
            return max(piles)


        start = 1
        end = max(piles)

        min_k = None

        while start <= end:
            mid = (start+end) // 2

            if canFinish(mid):
                min_k = mid
                end = mid - 1
            
            else:
                start = mid + 1
                

        return min_k