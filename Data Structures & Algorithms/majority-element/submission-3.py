class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashMap = {}

        n = len(nums)
        
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        for key, value in hashMap.items():
            if value > n / 2:
                return key
        