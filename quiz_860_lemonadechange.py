class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0 

        for bill in bills :
            if bill == 5 :
                five += 1 
            elif bill == 10 : 
                if five == 0 :
                    return False 
                five -= 1 
                ten += 1 
            else : 
                if ten > 0 and five > 0 :
                    ten -= 1 
                    five -=1 
                elif five >= 3  :
                    five -=  3
                else : 
                    return False 
        return True
