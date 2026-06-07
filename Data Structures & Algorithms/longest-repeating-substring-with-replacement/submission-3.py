class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0

        for c in charSet:
            l=0
            unmatchingCount = 0
            for r in range(len(s)):
                if s[r]!=c:
                    unmatchingCount+=1
                
                while unmatchingCount > k:
                    if s[l] != c:
                        unmatchingCount-=1
                    l+=1
                res=max(res, r-l+1)
            
        return res