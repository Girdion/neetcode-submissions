class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        # 3 4 5 6 1 2

        while l < r:
            m = (l + r) // 2
            print(nums[r], nums[m])
            if nums[r] < nums[m]:
                l = m + 1
                print(l)
            else:
                r = m
        
        return nums[l]

        