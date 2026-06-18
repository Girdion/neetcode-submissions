class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        freqChars = {}

        res = 0

        for char in chars:
            freqChars[char] = freqChars.get(char, 0) + 1
        
        for word in words:
            flag = 1

            freqWord = {}

            temp = freqChars.copy()

            for w in word:
                freqWord[w] = freqWord.get(w, 0) + 1
            
            print(freqWord)
            print(temp)
            for w in word:
                if w not in temp:
                    flag = 0
                    break
                else:
                    temp[w] -= 1
                    if temp[w] < 0:
                        flag = 0
                        break
            
            if flag: 
                res += len(word)

        return res

            

            

        