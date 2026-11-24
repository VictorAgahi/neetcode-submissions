class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        minimum_number_interval, maximum_number_interval = intervals[0][0], intervals[0][1]
        res = []
        index = 1
        n = len(intervals)


        while index < n:
            candidate_minimum, candidate_maximum = intervals[index]
            if candidate_minimum <= maximum_number_interval: 
                if candidate_maximum > maximum_number_interval:
                    maximum_number_interval = candidate_maximum
            else:
                res.append([minimum_number_interval, maximum_number_interval])
                minimum_number_interval = candidate_minimum
                maximum_number_interval = candidate_maximum
            index += 1
        res.append([minimum_number_interval, maximum_number_interval])
        return res

                
        