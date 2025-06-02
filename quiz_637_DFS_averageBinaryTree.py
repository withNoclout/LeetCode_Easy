class Solution : 

    def averageOfLevels(root):
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.pop(0)
                level_sum += node.val
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate average for current level
            level_avg = float(level_sum) / level_size
            result.append(level_avg)
        
        return result
