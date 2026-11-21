class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # z x y z x y z
        seen = set()
        left = 0
        best_streak = 0
        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            best_streak = max(best_streak, right - left + 1)
        return best_streak
            