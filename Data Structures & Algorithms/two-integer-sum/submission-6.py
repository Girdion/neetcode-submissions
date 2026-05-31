class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            idx_1 = i
            needed_num = target - num
            if needed_num in nums[i + 1:]:
                idx_2 = nums.index(needed_num, i + 1)
                return [idx_1, idx_2]

        
        

