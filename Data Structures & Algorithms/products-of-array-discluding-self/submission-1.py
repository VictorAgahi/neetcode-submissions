class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        

        for ...
            for ... 
                
        1 -> [2 * 4 * 6]
        2 -> ...
        O(n2)

        prefix = 1
        [1,1,1,1]
        
        prefix = 1 * 1
        -> add prefix before multiply

        prefix = 2
        -> add prefix before multiply

        prefix = 8 (if we are on the 3 rd index)
        prefix =  -> 48

        [1, 2, 4, ]

        suffix = 1

        """
        n = len(nums)
        res = [1] * n
        prefix = 1

        # [1, 1, 1, 1]
        for index, num in enumerate(nums):
            res[index] = prefix
            prefix *= num

        # [1, 1, 2, 8]

        suffix = 1 
        for i in range(n - 1, -1 , -1):
            res[i] *= suffix
            suffix *= nums[i]
        # [48, 24, 12, 8]
        
        return res
        