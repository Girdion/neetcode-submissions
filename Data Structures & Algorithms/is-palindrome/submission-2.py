class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_transformed = ""

        for i in range(len(s)):
            if s[i].isalnum():
                s_transformed += s[i]
        
        s_transformed = s_transformed.lower()

        low, high = 0, len(s_transformed)-1
        
        for i in range(len(s_transformed)):
            if s_transformed[low] == s_transformed[high]:
                low += 1
                high -= 1
            else:
                return False
        
        return True

        