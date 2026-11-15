import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = {}   
        for num in nums:
            if num in dico:
                dico[num] += 1
            else:
                dico[num] = 1
        heap = []
        for key, value in dico.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        l = []
        for item in heap:
            l.append(item[1])
        return l