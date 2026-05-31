class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        r = len(s)-1

        for i in range(len(s)//2):
            s[i], s[r] = s[r], s[i]
            r -= 1
        