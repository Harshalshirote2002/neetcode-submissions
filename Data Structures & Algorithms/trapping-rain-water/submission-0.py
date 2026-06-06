class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        n = len(height)
        i=0
        for i in range(n):
            if i == 0:
                continue

            start = i-1
            end = i+1
            left = -1
            right = -1
            while start>=0:
                if height[start] > left:
                    left = height[start]
                start-=1
            
            while end<=n-1:
                if height[end] > right:
                    right = height[end]
                end+=1
            
            if left>0 and right>0:
                currentHeight = min(left, right) - height[i]
                if currentHeight > 0:
                    total += currentHeight

        return total

            