#Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i=1
        while(i<len(intervals)):
            if intervals[i-1][1]>=intervals[i][0]:
                if intervals[i-1][1]<intervals[i][1]:
                    intervals[i-1][1]=intervals[i][1]
                intervals.pop(i)
            else:
                i+=1
        return intervals
        
