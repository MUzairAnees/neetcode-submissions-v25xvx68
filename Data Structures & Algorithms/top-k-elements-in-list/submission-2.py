class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        kList = []
        
        for x in nums:
            seen[x] = 1 + seen.get(x, 0)

        for num, freq in seen.items():
            kList.append([freq, num])

        kList.sort()

        res = []
        while len(res) < k:
            res.append(kList.pop()[1])

        return res