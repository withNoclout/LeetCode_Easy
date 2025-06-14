class Solution:
    def arrayRankTransform(self, arr ):
        # Create a sorted set of unique elements to assign ranks
        sorted_unique = sorted(set(arr))
        
        # Create a dictionary mapping each number to its rank
        rank_map = {num: i + 1 for i, num in enumerate(sorted_unique)}
        
        # Replace each element with its rank
        return [rank_map[num] for num in arr]
