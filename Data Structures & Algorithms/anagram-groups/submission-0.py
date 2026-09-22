class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for x in strs:
            sorted_s = "".join(sorted(x))
            anagram_map[sorted_s].append(x)
        return list(anagram_map.values())