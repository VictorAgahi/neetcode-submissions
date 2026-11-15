class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenElement = set()
        for num in nums:
            if num in seenElement:
                return True
            seenElement.add(num)
        return False