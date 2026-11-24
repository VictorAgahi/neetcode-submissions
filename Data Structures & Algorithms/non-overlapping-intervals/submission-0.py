class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        the idea here is to check if we have an overlap
        could be interesting to have a sorted list on the x element like : [X, _]
        then we check for the current interval [X, Y] 
        if the second interval [A, B] and A < Y
           -> we add 1 to the 
           -> Y = min (Y, B)
        else
            we check if A >= Y:
                then we have the current_min = X
            we take X which is the cuurent_min and the max(Y, B) as the new current_max
        
        
        TEST [1, 2] [3, 4] -> 0
        TEST [1, 2] [2, 3] -> 0
        TEST [1, 4] [2, 4] -> 1
        TEST [1, 10], [2, 3] -> 1
        """

        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        index = 1
        count = 0
        x, y = intervals[0]
        while index < n:
            a, b = intervals[index]
            if a < y:
                count += 1
                y = min(y,b)
            else:
                x, y = a, b
            index += 1
        return count
                    