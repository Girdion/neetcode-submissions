class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        freqs1, freqs2 = {}, {}

        for char in s1:
            freqs1[char] = freqs1.get(char, 0) + 1
        
        k = len(s1)

        for i in range(k):
            freqs2[s2[i]] = freqs2.get(s2[i], 0) + 1

        if freqs2 == freqs1:
            return True
        else:
            for r in range(k, len(s2)):
                left_char = s2[r-k]
                freqs2[left_char] -= 1

                if freqs2[left_char] == 0:
                    del freqs2[left_char]
                
                freqs2[s2[r]] = freqs2.get(s2[r], 0) + 1

                if freqs1 == freqs2: return True
        
        return False
