class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1 and flowerbed[-1] == 0: return True

        if flowerbed[0] == 0 and flowerbed[1] == 0: n -= 1

        if n == 0: return n == 0

        if flowerbed[-1] == 0 and flowerbed[len(flowerbed)-2] == 0: n -= 1

        if n == 0: return n == 0

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and (flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                n -= 1
                flowerbed[i] = 1
                if n == 0: break
        

        
        return n == 0
        