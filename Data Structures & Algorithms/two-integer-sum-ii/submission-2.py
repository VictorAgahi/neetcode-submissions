class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dico = {}
        t = target
        for index, num in enumerate(numbers):
            if num in dico: return [dico[num], index + 1]
            else:
                dico[t - num] = index + 1
        return []


        