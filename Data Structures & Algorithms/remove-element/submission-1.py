class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        point = 0

        for num in nums:
            if num != val:
                nums[point] = num
                point += 1
        
        return point
        

        