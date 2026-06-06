class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [1]
        suffixArr = [1]

        for num in nums:
            newNum = prefixArr[-1] * num
            prefixArr.append(newNum)

        for num in nums[::-1]:
            newNum = suffixArr[-1] * num
            suffixArr.append(newNum)
        
        prefixArr = prefixArr[1:]
        suffixArr = suffixArr[::-1][:-1]
        output_arr = [suffixArr[1]]
        for i in range(1, len(nums)-1):
            output_arr.append(prefixArr[i-1]*suffixArr[i+1])
        output_arr.append(prefixArr[-2])
        return output_arr
        
