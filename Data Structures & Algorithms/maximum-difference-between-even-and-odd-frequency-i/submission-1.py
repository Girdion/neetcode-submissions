class Solution:
    def maxDifference(self, s: str) -> int:
        mapS = {}

        for char in s:
            mapS[char] = mapS.get(char, 0) + 1
        
        oddFreq, evenFreq = [], []

        for key, value in mapS.items():
            if value % 2 == 1: oddFreq.append(value)
            else: evenFreq.append(value)
              
        a1, a2 = max(oddFreq) - min(evenFreq) , abs(min(oddFreq) - max(evenFreq))

        return a1
