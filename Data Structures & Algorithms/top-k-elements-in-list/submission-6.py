class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        buckets = [[] for _ in range(n)]

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, v in freq.items():
            buckets[v-1].append(key)

        res = []    
        cnt = 0
        print(buckets)
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    cnt += 1
                    if(cnt == k): return res
                


        