class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}

        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1

        topKFrequent = sorted(numDict, key=numDict.get, reverse=True)

        return topKFrequent[:k]
        
        
            
        

        


        