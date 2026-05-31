class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = []

        for i in range(len(temperatures)-1):
            cnt = 0
            flag = 0
            for j in range(i+1, len(temperatures)):
                cnt += 1

                if temperatures[j] > temperatures[i]:
                    flag = 1
                
                if flag == 1:
                    res.append(cnt)
                    break
                
                if flag == 0 and j == len(temperatures)-1:
                    res.append(0)
        
        res.append(0)
        
        return res


        