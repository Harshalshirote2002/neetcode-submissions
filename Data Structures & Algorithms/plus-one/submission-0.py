class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        n=len(digits)
        i =  n-1
        while i>=0:
            first = digits[i]
            power_10 = 10**(n-i-1)
            num += first * power_10
            i-=1

        num = str(num+1)
        res = []
        for i in num:
            res.append(int(i))

        return res
