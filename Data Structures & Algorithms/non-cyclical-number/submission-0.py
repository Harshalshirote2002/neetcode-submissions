class Solution:
    def isHappy(self, n: int) -> bool:
        encountered = []
 
        def identifier(n):
            tot = 0

            while n:
                val = n%10
                tot += val*val
                n//=10

            if tot == 1:
                return True
            else:
                nonlocal encountered
                if tot in encountered:
                    return False
                else:
                    encountered.append(tot)
                    return identifier(tot)

        return identifier(n)