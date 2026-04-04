class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        tripletArr = []
        nums.sort()

        for i in range(len(nums)):

            #avoid i dupes if i is not on index0 and if current i != last i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                total = nums[i]+nums[left]+nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    tripletArr.append([nums[i],nums[left],nums[right]])
                    left += 1

                    #avoid leftP dupes by checking current left with last left 
                    #while loop still valid. 
                    #right automatically force away from dupe since math not same
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return tripletArr
                    