class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        firstArr = nums[:k]

        print(firstArr)

        minimum = max(firstArr) - min(firstArr)
        mostMinimum = minimum

        for right in range(k, len(nums)):
            firstArr.pop(0)
            firstArr.append(nums[right])

            minimum = max(firstArr) - min(firstArr)
            mostMinimum = min(mostMinimum, minimum)
        
        return mostMinimum
        