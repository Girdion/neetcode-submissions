class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 3 4 5 6
        # 7 - 3 = 4
        # append ke hashmapnya, keynya value dari angka di loop tsb
        # lalu valuenya itu index
        # nah, kalo di loop kedua kan dia bkl lakuin 7 - 4 = 3
        # 3 itu ada di hashmap, artinya ada dua angka yang kalo ditambahin itu bkl sama dengan target, nah jadi return index skrg sama value dari key (complementnya)


        hashMap = {}

        for i in range(len(nums)):

            if target - nums[i] not in hashMap:
                hashMap[nums[i]] = i
            elif target - nums[i] in hashMap:
                return [hashMap[target-nums[i]], i]
        
        