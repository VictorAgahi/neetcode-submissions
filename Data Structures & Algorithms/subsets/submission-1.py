class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_list = []

        def backtrack(start):
            res.append(current_list[:])
            for i in range(start, len(nums)):
                current_list.append(nums[i])
                backtrack(i + 1)
                current_list.pop()
             
        backtrack(0)
        return res