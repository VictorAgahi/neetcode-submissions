class Solution:
    def is_pal(self, s1: str) -> bool:
        begin, end = 0, len(s1) - 1
        while begin < end:
            if s1[begin] != s1[end]:
                return False
            begin += 1
            end -= 1
        return True

        
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current_list = []
        def backtrack(start):
            if start == len(s):
                res.append(current_list[:])
                return

            for end in range(start, len(s)):
                substring = s[start : end + 1]
                if self.is_pal(substring):
                    current_list.append(substring)
                    backtrack(end + 1)
                    current_list.pop()
                    
        backtrack(0)
        return res
                    