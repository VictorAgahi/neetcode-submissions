import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        reversed_heap = [-x for x in stones] 
        heapq.heapify(reversed_heap)
        output = 0
        while len(reversed_heap) > 1:
            h1 = heapq.heappop(reversed_heap) 
            h2 = heapq.heappop(reversed_heap)  

            if h1 != h2:
                heapq.heappush(reversed_heap, h1 - h2)  # -8 - (-7) = -1

        return -reversed_heap[0] if reversed_heap else 0