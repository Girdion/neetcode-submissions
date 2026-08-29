class Solution {
    public boolean isAnagram(String s, String t) {

        Map<Character, Integer> freqS = new HashMap<>();
        Map<Character, Integer> freqT = new HashMap<>();

        for (char c : s.toCharArray()) {
            if (freqS.containsKey(c)) {
                freqS.put(c, freqS.get(c) + 1);
            } else {
                freqS.put(c, 1);
            }
        }

        for (char c : t.toCharArray()) {
            if (freqT.containsKey(c)) {
                freqT.put(c, freqT.get(c) + 1);
            } else {
                freqT.put(c, 1);
            }
        }
        
        return freqS.equals(freqT);
    }
}
