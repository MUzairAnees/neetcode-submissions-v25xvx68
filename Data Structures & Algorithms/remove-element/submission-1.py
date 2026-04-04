class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #get length
        length = len(nums)

        #set pointers to idx 0
        x,y = 0,0

        #enter the read loop
        while x < length:
            
            #enter the write loop
            while x < length and nums[x] != val:
                
                #if write loop was entered then we update value at pointer y (starting at idx 0 while x moves as it does) and move them both to next idx
                nums[y] = nums[x]
                x += 1
                y += 1
            
            #if write loop couldn't be entered or broken then we need to move the x pointer idx to check next idx
            x += 1
        
        return y