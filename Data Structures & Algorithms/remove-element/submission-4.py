class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[read] = nums[i]
                read += 1
        
        return len(nums[:read])
        