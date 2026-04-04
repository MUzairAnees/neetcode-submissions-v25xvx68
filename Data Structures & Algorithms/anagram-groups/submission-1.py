class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            temp = "".join(sorted(s))

            if temp not in groups:
                groups[temp] = [s]
            else:
                groups[temp].append(s)
            
            # groups[temp].append(s)

        return list(groups.values())