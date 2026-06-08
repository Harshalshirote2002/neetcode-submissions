class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))

        n = len(s1)

        l = 0
        r = n-1

        if len(s2) < len(s1):
            return False

        while r<len(s2):
            part = s2[l:r+1]
            sorted_part = "".join(sorted(part))

            if sorted_part == sorted_s1:
                return True
            r+=1
            l+=1
        
        return False