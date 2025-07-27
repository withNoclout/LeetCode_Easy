class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for fruit in fruits:
            fruit_unplaced = True
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    fruit_unplaced = False
                    break
            if fruit_unplaced:
                unplaced += 1
        return unplaced
