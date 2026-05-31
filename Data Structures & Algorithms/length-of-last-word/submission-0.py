class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed_s = s.strip()

        print(trimmed_s.split())

        return len(trimmed_s.split()[-1])
        