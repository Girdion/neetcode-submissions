class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""

        for char in s:
            if char.isalnum():
                new_s += char

        palindrome_checker = ""
        length = len(new_s)
        for i in range(length-1, -1, -1):
            palindrome_checker += new_s[i]
            
        return new_s == palindrome_checker