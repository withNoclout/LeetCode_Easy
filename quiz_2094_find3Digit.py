from itertools import permutations
class Solution : 
    def findEvenNumbers(self , digits):
        res = set()
        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                res.add(a * 100 + b * 10 + c)
        return sorted(res)
