class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        best_sequence = 0
        left = 0
        max_freq = 0

        for right in range(len(s)): 
            char = s[right]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            max_freq = max(max_freq, count[char]) 

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            best_sequence = max(best_sequence, right - left + 1)

        return best_sequence