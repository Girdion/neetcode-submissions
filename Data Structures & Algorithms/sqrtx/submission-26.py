class Solution:
    def mySqrt(self, x: int) -> int:

        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13
        # T T T T F F F F F F

        if x == 0 or x == 1:  return x

        l, r = 0, x

        while l < r:

            m = (l + r) // 2

            if m * m > x:
                r = m
            else:
                l = m + 1
        
        return r-1


