class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums: List[int], target: int) -> int:
            begin = 0
            end = len(nums) - 1
            while begin <= end:
                mid = (begin + end) // 2
                if nums[mid] == target:
                    return mid
                if target < nums[mid]:
                    end = mid - 1
                else:
                    begin = mid + 1
            return -1
            
        begin = 0
        end = len(matrix) - 1
        while begin <= end:
            mid = (begin + end) // 2
            mid_len = len(matrix[mid]) - 1
            if matrix[mid][0] <= target <= matrix[mid][mid_len]:
                output = search(matrix[mid], target)
                return output != -1 
            if target < matrix[mid][0]:
                end = mid - 1
            else:
                begin = mid + 1
        return False