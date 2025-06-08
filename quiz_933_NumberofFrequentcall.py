from collections import deque
class RecentCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.requests = deque()        


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
    

    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
