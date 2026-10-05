class Solution:
    def findLucky(self, arr: List[int]) -> int:

        hashMap = {}
        largest = -1

        for num in arr:

            hashMap[num] = hashMap.get(num, 0) + 1
        
        for k, v in hashMap.items():

            if k == v and v > largest:

                largest = v

        
        return largest


        
        