class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)

        temp = nums.copy()

        for i in range(len(nums)):
            nums[(i + k) % n] = temp[i]
        
        
        