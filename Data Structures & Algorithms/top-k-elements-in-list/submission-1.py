from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countList = defaultdict(list)
        count = 1  
        
       
        for index in range(len(nums) - 1): 
            if nums[index] == nums[index + 1]:  
                count += 1
            else:
                countList[nums[index]].append(count) 
                count = 1  

        
        countList[nums[-1]].append(count)

        
        sorted_countList = sorted(countList.items(), key=lambda x: sum(x[1]), reverse=True)

        result = []
        correctAns = []
        for number, counts in sorted_countList:
            result.append(number)
            
        for i in range(k):
            correctAns.append(result[i])
        
        return correctAns
