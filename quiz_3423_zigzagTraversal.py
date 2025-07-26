class Solution:
    def zigzagTraversal(self, grid):
        result = []
        skip = False

        for i, row in enumerate(grid):
            direction = row if i % 2 == 0 else row[::-1]
            for val in direction:
                if not skip:
                    result.append(val)
                skip = not skip

        return result
