class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        const = 0 
        for detail in details : 
            age = int(details[11:13])
            if age > 60 :
                count += 1 

        return count 
