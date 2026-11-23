class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)

        if n < 1 or len(intervals[0]) < 1:
            return [[]]
        intervals.sort(key=lambda x:x[0])
        current_min = intervals[0][0]
        current_max = intervals[0][1]
        index = 1
        while index < n:
            current_key_min, current_key_max = intervals[index]
            if current_min <= current_key_min <= current_max:
                if current_key_max > current_max:
                    current_max = current_key_max
            else:
                res.append([current_min, current_max])
                current_min = current_key_min
                current_max = current_key_max
            index += 1
        res.append([current_min, current_max])
        return res
                    

        
            