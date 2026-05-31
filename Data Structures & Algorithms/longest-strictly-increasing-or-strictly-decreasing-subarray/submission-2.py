class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 0, 0
        maxDec, maxInc = 0, 0

        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                dec = 0
                inc += 1
                maxInc = max(inc, maxInc)
            elif nums[i+1] < nums[i]:
                inc = 0
                dec += 1
                maxDec = max(dec, maxDec)
                print(maxDec)
            else:
                dec, inc = 0, 0
        
        return max(maxInc+1, maxDec+1)

