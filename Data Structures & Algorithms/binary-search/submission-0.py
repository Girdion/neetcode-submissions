class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            middle = (l + r) // 2
            value = nums[middle]

            if target > value:
                l = middle + 1
            elif target < value:
                r = middle - 1
            else:
                return middle
        
        return -1

        