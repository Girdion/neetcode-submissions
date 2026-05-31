class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        strs = sorted(strs, key=len, reverse=True)

        if len(strs) == 1: return strs[0]

        for char in strs:
            if char == "": return ""
  
        for i in range(len(strs[0])):
            valid = 1
            for j in range(1, len(strs)):
                char = strs[0][i]

                if strs[j][i] != char:
                    valid = 0
                    break
                
                if i+1 == len(strs[-1]) and j == len(strs)-1: 
                    if valid: 
                        res += char
                    valid = 0
                    break
                
            if valid: res += char

            else: break
        
        return res



        
        