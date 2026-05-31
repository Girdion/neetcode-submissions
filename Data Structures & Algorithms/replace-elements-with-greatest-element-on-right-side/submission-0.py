class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = 0
        res = []
        for i in range(len(arr)):
            max_num = 0
            if i == len(arr)-1:
                res.append(-1)
                break
            for j in range(i+1, len(arr)):
                if arr[j] >= max_num:
                    max_num = arr[j]
            res.append(max_num)
        return res

        
        