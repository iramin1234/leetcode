class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary keys are the letters of the anagram
        strs_dict = collections.defaultdict(list)

        for word in strs:
            anagram_key = [0] * 26
            for char in word:
                anagram_key[ord(char) - ord('a')] += 1
            strs_dict[tuple(anagram_key)].append(word)
        return strs_dict.values()
