#3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)-1):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[j]+nums[k]==-1*nums[i]:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k]>-1*nums[i]:
                    k-=1
                else:
                    j+=1
        return list(res)
            
        
        
