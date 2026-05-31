class Solution {
    /**
     * @param {string[]} arr
     * @param {number} k
     * @return {string}
     */
    kthDistinct(arr, k) {
        const freq = {}
        let cnt = 0;

        for(let char of arr){
            freq[char] = (freq[char] || 0) + 1;
        }


        for(let [key, value] of Object.entries(freq)) {
            if(value === 1) {
                cnt += 1;
                if(cnt === k) {
                    return key;
                }
            }
        }

        return "";
    }
}
