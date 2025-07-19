class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        tested = 0 
        n = len( batteryPercentages ) 

        for i in range( n ) :
            if batteryPercentages[i] >= 50 :
                tested += 1 

                for j in range( i + 1 , n ) :
                    batteryPercentages[j] = max(0 , batteryPercentages[j] - 1 )

        return tested
