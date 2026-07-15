class Solution:
    def sortColors(self, nums: List[int]) -> None:

        k = 0
        
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        while 0 in hashMap and hashMap[0] != 0:
            nums[k] = 0
            hashMap[0] -= 1
            k += 1
        
        while 1 in hashMap and hashMap[1] != 0:
            nums[k] = 1
            hashMap[1] -= 1
            k += 1
        
        while 2 in hashMap and hashMap[2] != 0:
            nums[k] = 2
            hashMap[2] -= 1
            k += 1
        


        