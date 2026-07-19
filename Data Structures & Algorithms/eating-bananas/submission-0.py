class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(speed: int) -> bool:
            total_hours = 0

            for pile in piles:
                total_hours += (pile + speed - 1) // speed

            return total_hours <= h

        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2

            if can_eat(m):
                r = m
            else:
                l = m + 1

        return l