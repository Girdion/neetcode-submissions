class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")

        cleaned_s = ""

        for char in s:
            if char.isalnum():
                cleaned_s += char

        left = 0
        right = len(cleaned_s) - 1

        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
        
        return True