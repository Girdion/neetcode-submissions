class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                return m

        if target not in nums and nums[l] < target:
            return l+1
        else:
            return l
                
        
       