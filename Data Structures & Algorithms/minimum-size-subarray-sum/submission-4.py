class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        minAns = len(nums)
        left = 0
        total = 0
        flag = 0

        for right in range(len(nums)):

            total += nums[right]

            while total >= target:
                flag = 1
                ans = right - left + 1
                minAns = min(ans, minAns)
                total -= nums[left]
                left += 1
            
            
        if not flag: return 0
        else: return minAns
            
        
            




