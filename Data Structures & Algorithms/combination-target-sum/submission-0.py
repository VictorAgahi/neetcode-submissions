from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current_list = []
        nums.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(current_list[:])
                return 
            if remaining < 0:
                return
            for i in range(start, len(nums)):
                if remaining < nums[i]:
                    break
                current_list.append(nums[i])
                backtrack(i, remaining - nums[i])
                current_list.pop()
            
                    
        backtrack(0, target) 
        return res
            