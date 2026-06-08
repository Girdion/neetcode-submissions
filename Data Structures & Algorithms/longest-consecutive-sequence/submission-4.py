class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCnt = 0

        for num in numSet:
            if num - 1 not in numSet:  
                cnt = 1
                while num + cnt in numSet:
                    cnt += 1
                maxCnt = max(cnt, maxCnt)

        return maxCnt