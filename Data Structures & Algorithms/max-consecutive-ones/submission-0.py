class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount, count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums)-1 and count > maxCount:
                    maxCount = count
            elif nums[i] == 0:
                if count > maxCount:
                    maxCount = count
                count = 0
        return maxCount


        