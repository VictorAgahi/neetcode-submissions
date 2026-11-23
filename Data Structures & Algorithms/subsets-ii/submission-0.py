from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_list = []
        nums.sort()
        def backtrack(start: int):            
            res.append(current_list[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current_list.append(nums[i])
                backtrack(i + 1)
                current_list.pop()

        backtrack(0)
        return res