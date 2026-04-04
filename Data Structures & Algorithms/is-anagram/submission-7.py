class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for c in s:
            seen[c] = seen.get(c, 0) + 1

        for c in t:
            seen[c] = seen.get(c, 0) - 1

        if all(v == 0 for v in seen.values()):
            return True
        else:
            return False        