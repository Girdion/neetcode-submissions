class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        majCnt = len(nums) // 3

        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for k, v in freq.items():
            if v > majCnt: 
                print(v)
                res.append(k)
        
        return res

        