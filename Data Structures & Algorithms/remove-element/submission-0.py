class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        length = len(nums)

        y = 0
        x = 0

        while x < length:
            while x < length and nums[x] != val:
                nums[y] = nums[x]
                x += 1
                y += 1
            x += 1

        return y