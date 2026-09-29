class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end-start)//2

            # print(nums[start], nums[end], nums[mid])

            if nums[mid] == target:
                return mid
            elif (target>= nums[0] and nums[mid] >= nums[0]) or (target <= nums[-1] and nums[mid] <= nums[-1]):
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid-1
            else:
                # print(target, mid)
                if target > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
                # print(start, end)

        return -1
