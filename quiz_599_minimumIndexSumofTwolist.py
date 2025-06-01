class Solution : 
    def findRestaurant( self , list1 , list2 ) :
        index_map = {} 
        for i in range( len(list1 )):
            index_map[list1[i] ] = i 

        min_sum = float('inf')
        result = [] 

        for j in range( len(list2) ) :
            word = list2[j]
            if word in index_map : 
                index_sum = j + index_map[word] 
                if index_sum < min_sum : 
                    result = [word]
                    min_sum = index_sum
                elif index_sum == min_sum: 
                    result.append(word) 

        return resulto

