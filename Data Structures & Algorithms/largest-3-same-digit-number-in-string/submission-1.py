class Solution:
    def largestGoodInteger(self, num: str) -> str:

        freq = 1
        maxNum = -1
        
        for i in range(len(num)-1):
            if num[i] == num[i+1]:
                freq += 1
                if freq == 3:
                    maxNum = max(maxNum, int(num[i]))
            else: freq = 1
        
        return str(maxNum) * 3 if maxNum >= 0 else ""


