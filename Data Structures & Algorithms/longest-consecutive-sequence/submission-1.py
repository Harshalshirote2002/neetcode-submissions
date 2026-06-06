class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len_found = 0
        for item in nums:
            
            found = True
            len_found = 1
            while len_found<len(nums) and found:
                item+=1
                if item in nums:
                    len_found += 1
                else:
                    found = False
            if len_found>max_len_found:
                max_len_found = len_found
                # print(max_len_found)
        
        return max_len_found