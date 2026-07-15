class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []

        for i in range(k):
            diff = abs(arr[i] - x)

            res.append(arr[i])
        
        for right in range(k, len(arr)):

            diff = abs(arr[right] - x)

            if diff < abs(res[0] - x):
                res.pop(0)
                res.append(arr[right])
        
        return res

