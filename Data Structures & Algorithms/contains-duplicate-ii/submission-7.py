class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = set()

        numsMap = {}

        for i in range(len(nums)):

            if nums[i] not in seen:
                seen.add(nums[i])
                numsMap[nums[i]] = i
            else:
                if abs(i - numsMap[nums[i]]) <= k: return True
                numsMap[nums[i]] = i
        
        return False
        