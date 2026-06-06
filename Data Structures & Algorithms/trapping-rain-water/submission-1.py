class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        n = len(height)

        prefixArr = [0]
        suffixArr = [0]

        for i in range(1, n):
            maxPrefix = prefixArr[-1]
            if height[i-1] > maxPrefix:
                prefixArr.append(height[i-1])
            else:
                prefixArr.append(maxPrefix)

            j = n-i-1
            maxSuffix = suffixArr[-1]
            if height[j+1] > maxSuffix:
                suffixArr.append(height[j+1])
            else:
                suffixArr.append(maxSuffix)


        suffixArr.reverse()



        for i in range(n):
            slabHeight = min(suffixArr[i], prefixArr[i]) - height[i]
            if slabHeight>0:
                total+=slabHeight

        return total

            