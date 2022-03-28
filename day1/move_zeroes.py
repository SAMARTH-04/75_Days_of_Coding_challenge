#Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=0
        l=0
        while(l<len(nums)):
            l+=1
            if nums[r]==0:
                pop=nums.pop(r)
                nums.append(pop)
            else:
                r+=1
        return nums
