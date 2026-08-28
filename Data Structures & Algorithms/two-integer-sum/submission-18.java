
// HashMap
// Integer -> Integer
// Key: Number, Value: Index
// Complement => Target - Num is in HashMap, kita return current index
// sama return HashMap[complement]

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> hashMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if(hashMap.containsKey(complement)){
                return new int[]{hashMap.get(complement), i};
            } else {
                hashMap.put(nums[i], i);
            }
        }

        return new int[]{};
    }
}
