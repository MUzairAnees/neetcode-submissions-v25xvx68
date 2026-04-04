class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        x = y = 0

        while x < length:
            nums[y] = nums[x]
            while x < length and nums[x] == nums[y]:
                x += 1
            y += 1

        return y