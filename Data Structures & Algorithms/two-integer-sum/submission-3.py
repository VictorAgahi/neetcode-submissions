from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}
        for index, num in enumerate(nums):
            if num in dico:
                return [dico[num], index]
            else:
                dico[target - num] = index
                
        return []
