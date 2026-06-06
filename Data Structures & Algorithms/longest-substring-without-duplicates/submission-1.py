class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestString = ""
        n = len(s)
        i=0
        maxLength = 0
        while i<n:
            if s[i] not in longestString:
                longestString+=s[i]
                i+=1
                currentLength = len(longestString)
                if currentLength>maxLength:
                    maxLength=currentLength
            else:
                currentLength = len(longestString)
                if currentLength>maxLength:
                    maxLength=currentLength
                longestString = longestString[1:]

        return maxLength