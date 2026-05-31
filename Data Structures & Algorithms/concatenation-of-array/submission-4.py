class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArr = nums

        for i in range(len(nums)):
            newArr.append(nums[i])
        
        return newArr
        