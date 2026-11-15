from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            dico[key].append(s)
            
        return list(dico.values())