class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in range(len(nums1)):

            idx = nums2.index(nums1[i])

            valid = False

            while idx < len(nums2):
                if nums2[idx] > nums1[i]:
                    res.append(nums2[idx])
                    valid = True
                    break
                idx += 1
            
            if not valid: res.append(-1)
        
        return res
        