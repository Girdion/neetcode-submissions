class Solution:
    def isPathCrossing(self, path: str) -> bool:

        origin = [0, 0]

        visitedOrigins = []

        for p in path:
            if p == 'N':
                origin[1] += 1
            elif p == 'S':
                origin[1] -= 1
            elif p == 'E':
                origin[0] -= 1
            elif p == 'W':
                origin[0] += 1

            if origin in visitedOrigins or (origin[0] == 0 and origin[1] == 0): 
                return True    
            
            visitedOrigins.append(origin.copy())
            

        return False
        