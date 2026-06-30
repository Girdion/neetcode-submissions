class Solution:
    def findLucky(self, arr: List[int]) -> int:

        hashMap = {}

        maxNum = -1

        for num in arr:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for k, v in hashMap.items():
            if k == v: maxNum = max(maxNum, v)
        
        if maxNum > 0: return maxNum

        return -1
        