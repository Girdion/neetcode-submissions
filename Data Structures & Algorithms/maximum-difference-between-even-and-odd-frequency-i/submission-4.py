class Solution:
    def maxDifference(self, s: str) -> int:
        mapS = {}

        for char in s:
            mapS[char] = mapS.get(char, 0) + 1
        
        oddFreq, evenFreq = [], []

        for value in mapS.values():
            if value % 2 == 1: oddFreq.append(value)
            else: evenFreq.append(value)
              
        a1 = max(oddFreq) - min(evenFreq)

        return a1
