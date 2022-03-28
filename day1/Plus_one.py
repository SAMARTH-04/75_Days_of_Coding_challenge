#Plus one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in range(len(digits)):
            s+=str(digits[i])
        s=int(s)
        s+=1
        s=str(s)
        res=[]
        for i in s:
            res.append(i)
        return res
