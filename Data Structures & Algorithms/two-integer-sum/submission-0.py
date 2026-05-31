class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        for index_i, num_i in enumerate(nums):
            for index_j, num_j in enumerate(nums):
                if(index_i != index_j and num_i + num_j == target):
                    indexes.append(index_i)
                    indexes.append(index_j)
                    return indexes

        