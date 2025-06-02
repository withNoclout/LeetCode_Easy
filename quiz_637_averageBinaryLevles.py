from collections import deque

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])  # ใช้ queue ทำ BFS

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            average = level_sum / level_count
            result.append(average)

        return result

