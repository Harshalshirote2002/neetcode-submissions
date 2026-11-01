class Solution:
    def hammingWeight(self, n: int) -> int:
        rep = bin(n)[2:]
        res = 0
        for char in rep:
            if char == "1":
                res+=1

        return res