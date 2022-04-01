#Subarray Sum Equals K
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        add=0
        d={}
        d[0]=1
        for i in range(len(nums)):
            add+=nums[i]
            if add-k in d:
                cnt+=d[add-k]
                if add in d:
                    d[add]+=1
                else:
                    d[add]=1
            else:
                if add in d:
                    d[add]+=1
                else:
                    d[add]=1
        print(d)
        return cnt
            
            
         
