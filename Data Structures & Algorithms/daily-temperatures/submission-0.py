class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        THINKING:
        temperametures [DAY_1, ..., DAY_I]

        RETURN -> [DAY_WARMER_TEMPS_1, ..., DAY_WARMER_TEMPS_I]

        Basically [] -> [] and the length of temp = length of return array

        IDEA 1:
            O (n**2) -> for each element we check the first warmer next day
            We have 30 then we check the next day 29, 29 < 30 -> next day ... day n 30 < 31

            Not super optimal
        IDEA 2:
            Thinking about something like a binarary search with 2 pointers .. 
            Look complicated and not optimal -> list is_sorted
            Same for sliding windows not super efficient here 
        IDEA 3:
            We can use Stack to store the index of the hotest element
            basically for this example: [30,38,30,36,35,40,28]
            we add 0 on the queue which represente the only element

[30,38,30,36,35,40,28]
        """
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)

        return res

            
        