class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read, write = 0, 0

        while read < len(nums):
            if nums[read] == val:
                read += 1
            else:
                nums[write] = nums[read]
                read += 1
                write += 1
        
        return write