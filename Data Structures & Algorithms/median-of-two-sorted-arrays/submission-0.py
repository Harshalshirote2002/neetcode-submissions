class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sortedArr = []

        while nums1 and nums2:
            if nums1[0] > nums2[0]:
                sortedArr.append(nums2[0])
                nums2 = nums2[1:]
            elif nums1[0] < nums2[0]:
                sortedArr.append(nums1[0])
                nums1 = nums1[1:]

            else:
                sortedArr.append(nums1[0])
                sortedArr.append(nums2[0])
                nums1 = nums1[1:]
                nums2 = nums2[1:]

        while nums1:
            sortedArr.append(nums1[0])
            nums1 = nums1[1:]

        while nums2:
            sortedArr.append(nums2[0])
            nums2 = nums2[1:]

        n = len(sortedArr)
        if n%2 == 0:
            return (sortedArr[(n-1)//2] + sortedArr[n//2])/2
        else:
            return sortedArr[n//2]