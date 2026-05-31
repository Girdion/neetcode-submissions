class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        for j in range(len(nums)):
            if nums[j] not in seen:
                seen.add(nums[j])
                if nums[i] in seen:
                    nums[i] = nums[j]
                i += 1
            
        return i
            
            

        