class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ptr, res = 0, 0

        if len(s) == 0: return 0

        s.sort(reverse=True)
        g.sort(reverse=True)

        for i in range(len(g)):
            if g[i] <= s[ptr]:
                res += 1
                ptr += 1
                if ptr == len(s): break
        
        return res
        