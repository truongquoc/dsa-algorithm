import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for n in nums:
            counter[n]+=1
        
        max_heap = []
        res=[]

        for item,freq in counter.items():
            heapq.heappush(max_heap, (-freq, item))
        
        for _ in range(k):
            freq,value = heapq.heappop(max_heap)
            res.append(value)
        return res