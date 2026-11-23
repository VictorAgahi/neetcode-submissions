class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        current_list = []
        candidates.sort()
        def backtrack(start, remaining):
            if remaining == 0:
                res.append((current_list[:]))
                return
            if remaining < 0:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                current_list.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                current_list.pop()
        backtrack(0, target)
        return res
