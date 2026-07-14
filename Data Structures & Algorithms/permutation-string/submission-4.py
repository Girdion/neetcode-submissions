class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)

        s1 = list(s1)

        s1.sort()

        s2 = list(s2)

        if s1 == sorted(s2[:k]): return True

        s2s = s2[:k]

        for i in range(k, len(s2)):
            s2s.pop(0)
            s2s.append(s2[i])

            if s1 == sorted(s2s): return True
        
        return False
            

        