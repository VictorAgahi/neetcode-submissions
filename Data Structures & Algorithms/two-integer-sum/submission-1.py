from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = defaultdict(list)
        for index, num in enumerate(nums):
            dico[num].append(index)
        for key, values in dico.items():
            targetInDico = target - key
            if targetInDico == key: # case [5,5] & target = 10
                if len(values) > 1: return [values[0], values[1]]
            elif targetInDico in dico:
                return [values[0], dico[targetInDico][0]]
        return []
            