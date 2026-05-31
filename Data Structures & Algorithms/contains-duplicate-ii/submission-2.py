class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1, 2, 3, 4, 5, 6, 6

        numMap = {}

        for i, num in enumerate(nums):
            if num not in numMap:
                numMap[num] = i
            else:
                if abs(numMap[num] - i) <= k:
                    return True
                else:
                    numMap[num] = i
        print(numMap)
        return False
        

            
        