class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        def get_high( start_color , other_color )  :
            height = 0 
            curr_red = red 
            curr_blue = blue 
            for i in range( 100 ) :
                balls_need = i + 1 
                if i % 2 ==0 :
                    if start_color == 'red' :
                        if curr_red >= balls_need : 
                            curr_red -= balls_need 
                            height +=1 
                        else : 
                            break 
                    else : 
                        if curr_blue >= balls_need :
                            curr_blue -= balls_need 
                            height += 1 
                        else : 
                            break 
                else :
                    if start_color =='red' :
                        if curr_blue >= balls_need : 
                            curr_blue -= balls_need 
                            height += 1 
                        else : 
                            break 
                    else : 
                        if curr_red >= balls_need : 
                            curr_red -= balls_need 
                            height +=1 
                        else: 
                            break 

            return height 
        
        return max( get_high('red', 'blue') , get_high('blue', 'red') )
