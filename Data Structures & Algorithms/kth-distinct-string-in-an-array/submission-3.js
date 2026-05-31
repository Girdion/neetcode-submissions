class Solution {
    /**
     * @param {string[]} arr
     * @param {number} k
     * @return {string}
     */
    kthDistinct(arr, k) {
        const freq = {};

        for (let word of arr) {
            freq[word] = (freq[word] || 0) + 1;
        }

        let count = 0;

        for (let word of arr) {
            if (freq[word] === 1) {
                count++;
                if (count === k) {
                    return word;
                }
            }
        }

        return "";
    }
}
