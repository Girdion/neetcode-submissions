class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, len(numbers)-1
        for i in range(len(numbers)):
            if numbers[ptr1] + numbers[ptr2] < target:
                ptr1 += 1
            elif numbers[ptr2] + numbers[ptr1] > target:
                ptr2 -= 1
            elif numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1+1, ptr2+1]
            
            


        
        