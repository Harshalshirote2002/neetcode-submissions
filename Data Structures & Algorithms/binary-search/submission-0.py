class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) -1

        if start==end:
            if nums[0] == target:
                return 0

        while start<=end:
            mid = int((start + end)/2)

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                print(nums[mid], mid)
        
        return -1