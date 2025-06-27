class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        from collections import defaultdict , deque 
        
        graph = defaultdict(list ) 
        for u ,v in edges : 
            graph[u].append(v) 
            graph[v].append(u)

        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue : 
            node = queue.popleft()
            if node == destination : 
                return True 
            for neighbor in graph[node] :
                if neighbor not in visited : 
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False 
