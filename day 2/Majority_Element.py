#Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)//2
        #x=nums.count(num[n])
        return(nums[n])
        
