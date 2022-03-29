#Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls=0
        rs=sum(nums)-nums[0]
        ind=0
        while(ls!=rs) and ind<len(nums):
            ls+=nums[ind]
            ind+=1
            if ind<len(nums):
                rs-=nums[ind]
        print(ls)
        print(rs)
        if ind==len(nums):
            return -1
        else:
            return ind
            
            
        
