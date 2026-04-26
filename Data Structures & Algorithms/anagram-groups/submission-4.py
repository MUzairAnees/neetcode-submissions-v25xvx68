from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            anagram[sortedS].append(s)
        return list(anagram.values())