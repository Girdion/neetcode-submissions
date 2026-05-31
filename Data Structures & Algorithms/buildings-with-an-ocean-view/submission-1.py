class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = heights[len(heights)-1]
        res = [len(heights)-1]

        for i in range(len(heights)-2, -1, -1):
            if heights[i] > maxHeight:
                maxHeight = heights[i]
            
            res.append(i)

            if heights[res[-1]] < maxHeight or heights[res[-1] + 1] == maxHeight:
                res.pop()
     
        res.sort()

        return res
