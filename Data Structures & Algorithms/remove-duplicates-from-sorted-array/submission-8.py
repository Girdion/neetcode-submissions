class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = set()

        write = 0

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[write] = nums[i]
                write += 1
        
        return write
            
                
            
            

            



        
            