class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        res = 0

        for i in range(k):
            if blocks[i] == 'W':
                res += 1
        
        minRes = res

        for right in range(k, len(blocks)):

            if blocks[right] == 'W':
                res += 1
            
            if blocks[right - k] == 'W':
                res -= 1
            
            minRes = min(res,minRes)

        return minRes


        