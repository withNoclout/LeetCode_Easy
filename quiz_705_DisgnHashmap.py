class MyHashSet( object ) :
    def __init__( self ) :
        self.size  = 1000 
        self.buckets = [ [] for _ in range(self.size ))]

    def _hash( self , key ) :

        return key % self.size 
    
    def add( self , key ):

        index = self._hash(key)
        if key not in self.buckets[index ] : 
            self.buckets[index].append(key) 

    def remove( self , key ) :
        index = self._hash(key)
        if key in self.buckets[index ] :
            self.buckets[index].append(key) 


    def remove( self , key ) :

        index = self._hash(key )
        if key in self.buckets[index ] :
            self.buckets[index ].remove(key)

    def contains( self , key ) :
        index = self._hash(key) 
        return key in self.buckets[index ]
