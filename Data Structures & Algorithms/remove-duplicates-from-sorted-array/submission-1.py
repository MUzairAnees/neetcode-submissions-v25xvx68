class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        x,y = 0,0

        #enter the read loop always, exits by itself after traversing the entire length
        while x < length:
            
            #if this line is placed at the end then x pointer will try to read a value outside the idxs of the list causing an out of range error
            nums[y] = nums[x]
            
            #enter the write loop, only if x has not traversed the entire length AND if value at y pointer and if value at x pointer IS THE SAME 
            #(meaning now x has to check next value and if duplicate then skip)
            while x < length and nums[y] == nums[x]:
                #increase x pointer by 1 to check if the next value is a duplicate or not
                x += 1
                #when value at x pointer is finally not a duplicate then exit the write loop
            
            #when it exits after the write loop, then x pointer is at a different value than value at y pointer
            #so increase y pointer by 1 so that you don't overwrite current value at y pointer and writing at the next y pointer idx
            y += 1
            
            #once y pointer is on unwritten idx value and x pointer is on non duplicate value, update values next outer loop check
            
        
        return y
