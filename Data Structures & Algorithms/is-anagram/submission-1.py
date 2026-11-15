class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dico = {}
        for char in s:
            if char in dico:
                dico[char] += 1
            else:
                dico[char] = 1
        for char in t:
            if char in dico:
                dico[char] -= 1
            else:
                return False
        for key, value in dico.items():
            if value != 0:
                return False
        return True
        