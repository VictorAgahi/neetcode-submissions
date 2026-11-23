from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_list = []
        used = [False] * len(nums)

        def backtrack():
            if len(current_list) == len(nums):
                res.append(current_list[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current_list.append(nums[i])
                backtrack()
                current_list.pop()
                used[i] = False
        backtrack()
        return res