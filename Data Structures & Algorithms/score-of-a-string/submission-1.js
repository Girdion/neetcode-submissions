class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    scoreOfString(s) {
        let sum = 0;
        for(let i = 0; i < s.length-1; i++){
            const curr = s.charCodeAt(i);
            const next = s.charCodeAt(i+1);
            const abs = Math.abs(curr-next);
            sum += abs;
        }
        return sum;
    }
}
