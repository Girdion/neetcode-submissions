class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        hashMap = {}
        flag = False
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                hashMap[nums[i]] = i
            else:
                
                if abs(hashMap[nums[i]] - i) <= k:
                    flag = True
                    return flag
                else:
                    hashMap[nums[i]] = i
        
        return flag
