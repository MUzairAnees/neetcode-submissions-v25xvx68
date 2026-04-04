class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaHash = defaultdict(list)

        for string in strs:
            word = "".join(sorted(string))

            anaHash[word].append(string)

        return list(anaHash.values())
            