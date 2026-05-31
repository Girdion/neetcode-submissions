class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()

        res = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                else:
                    res.append(grid[i][j])
        
        for num in list(seen):
            if num-1 not in seen and num != 1:
                res.append(num-1)
                break
            elif num+1 not in seen:
                res.append(num+1)
                break

        return res[:2]
        