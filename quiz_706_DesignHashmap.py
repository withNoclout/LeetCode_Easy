class MyHashMap( object ) :
    def __init__( self )  :
        self.size = 1000 
        self.buckets = [[] for _ in range( self.size)]

    def _hash( self , key ) : 
        return key % self.size  
    
    def put( self , key , value ) :
        index  = self._hash(key ) 

        for i , pair in enumerate( self.buckets[index ] ):
            if pair[0] == key:  
                self.buckets[index][i] = [ key , value ] 
                return 
            
        self.buckets[index].append([key , value ])

    def get( self , key ) :
        index = self._hash(key) 
        for pair in self.buckets[index] :
            if pair[0]  == key  : 
                return pair[1] 
            
        return -1 

    def remove( self , key ) :

        index =  self._hash(key) 

        for i  , pair in enumerate( self.buckets[index] ) : 
            if pair[0] == key : 
                self.buckets[index].pop(i) 
                return 
            
            
