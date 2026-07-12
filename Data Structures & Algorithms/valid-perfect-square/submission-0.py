class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        number = 0
        i = 1

        while number < num:
            number = i * i

            if number == num: return True

            i += 1
        
        return False
        