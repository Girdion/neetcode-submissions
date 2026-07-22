class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        for value in hashMap.values():

            if value % 2 == 1: return False

        return True
        