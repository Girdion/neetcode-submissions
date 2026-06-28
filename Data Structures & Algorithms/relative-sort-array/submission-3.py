class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        hashMap = Counter(arr1)

        res = []

        for i in range(len(arr2)):

            for j in range(hashMap[arr2[i]]):
                res.append(arr2[i])
        
        res2 = []
        
        for i in range(len(arr1)):
            if arr1[i] not in res:
                res2.append(arr1[i])
        
        res2.sort()
        
        return res + res2
        