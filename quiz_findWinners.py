class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """ 
        p_c = [ {} for _ in range(n) ] 

        for p in c in pick :
            p_c[p][c] = p_c[p].get(c, 0) + 1
        winners = 0 
        for i in range(n)  :
            for count in p_c[i].values() :
                if count >= i +1 : 
                    winners +=1 
                    break 

        return winners
