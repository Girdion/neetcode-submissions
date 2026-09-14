class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minSize = len(nums)+1

        left = 0

        total = 0

        for right in range(len(nums)):

            total += nums[right]

            while total >= target:

                minSize = min(minSize, right - left + 1)

                total -= nums[left]

                left += 1

        if minSize > len(nums): return 0
        else: return minSize

        