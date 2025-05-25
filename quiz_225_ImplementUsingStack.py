from collections import deque 

class MyStack( object ) : 
    def __init__(self ) : 
        self.q1 =  deque() 
        self.q2 = deque() 
        

    def push( self , x ) :  
        self.q2.append( x ) 
        while  self.q1  : 
            self.q2.append( self.q1.popleft())  
        self.q1 , self.q2  = self.q2 , self.q1  

    def pop(  self ) : 
        top = self.q1.popleft() 
        return top 
    
    def top(self )  :
        return self.q1[0]
    
    def empty( self )  : 
        is_empty =  not self.q1 
        return is_empty
    
