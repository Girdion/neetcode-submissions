class Solution:
    def maxScore(self, s: str) -> int:

        maxScore = 0

        setS = set(s)

        for i in range(1, len(s)):

            left = s[:i]
            right = s[i:]

            zeros = left.count('0')
            ones = right.count('1')

            maxScore = max(maxScore, zeros+ones)
        
        return maxScore

        