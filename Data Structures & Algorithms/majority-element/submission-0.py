class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         n = len(nums)
         num_to_count = {}
        
         for num in nums:
            num_to_count[num] = num_to_count.get(num, 0) + 1
            if num_to_count[num] > n // 2:
             return num
            