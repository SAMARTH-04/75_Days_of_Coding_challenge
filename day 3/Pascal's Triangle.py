#Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas, pre = [], []

        for i in range(1,numRows+1):
            row = [1] * i
            print(row)

            if len(row) > 2:
                for j in range(len(pre)-1):
                    row[j+1] = pre[j] + pre[j+1] 

            pre = row
            pas.append(row)
        return (pas)
        
        
