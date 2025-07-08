class Solution(object):


    def pickGifts(self , gifts, k):
        import heapq 
        import math 
        # Create a max-heap using negative values (since heapq is a min-heap by default)
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        # Perform k operations
        for _ in range(k):
            # Get the largest pile (remember to negate back the value)
            max_gift = -heapq.heappop(max_heap)
            # Calculate the new value for that pile
            new_gift = math.floor(math.sqrt(max_gift))
            # Push the new value back into the heap (negated to maintain max-heap)
            heapq.heappush(max_heap, -new_gift)
        
        # The total number of gifts remaining
        return -sum(max_heap)
