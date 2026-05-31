class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 0, 0
        maxDec, maxInc = 0, 0

        # inc = 1, maxInc = 1
        # dec = 1, maxDec = 1,
        # dec = 2, maxDec = 2
        # dec = 3, maxDec = 3
        # dec = 4, maxDec = 4
        # inc = 2, maxInc = 2
        # dec = 5, maxDec = 5


        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                dec = 0
                inc += 1
                maxInc = max(inc, maxInc)
                print("maxInc: ", maxInc)
            elif nums[i+1] < nums[i]:
                inc = 0
                dec += 1
                maxDec = max(dec, maxDec)
                print(maxDec)
            else:
                dec, inc = 0, 0
        
        return max(maxInc+1, maxDec+1)

