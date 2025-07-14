class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        distance = 0 
        while mainTank > 0 :
            if mainTank >=5 : 
                mainTank -= 5 
                distance += 50
                if additionalTank >= 1 :
                    additionalTank -= 1 
                    mainTank += 1 

            else : 
                distance += mainTank * 10 
                mainTank = 0 

        return distance 
