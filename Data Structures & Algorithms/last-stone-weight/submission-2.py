class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            largest = stones.pop()
            second_largest = stones.pop()

            if largest != second_largest:
                stones.append(largest - second_largest)

        return stones[0] if stones else 0