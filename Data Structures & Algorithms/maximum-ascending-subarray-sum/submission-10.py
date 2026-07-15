class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        total = nums[0]
        maxTotal = total

        for i in range(len(nums)-1):

            if nums[i+1] > nums[i]:
                total += nums[i+1]
            else:
                total = nums[i+1]
            
            maxTotal = max(total, maxTotal)
        
        return maxTotal
            
        
        