class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        if money < children : 
            return -1 
        
        money -= children
        full_eights = money //7 

        if full_eights > children  : 
            return children
        if full_eights == children : 
            return full_eights if money % 7 == 0 else full_eights - 1 
        

        remaining_money = money - full_eights * 7 
        if full_eights == children -1 and remaining_money == 3 :
            return full_eights - 1 
        
        return full_eights
