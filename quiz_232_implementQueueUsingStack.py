class MyQueue(object ) : 
    def __init__ ( self ) : 
        self.in_stack  = [] 
        self.out_stack = [] 

    def push(self , x ) : 
        self.in_stack.append(x)

    def pop(self ) : 
        self._move()
        return  self.in_stack.pop()

    def peek(self)  :
        self._move()
        return self.out_stack[-1]
    
    def empty (self) : 
        return not self.in_stack or not self.out_stack
    

    def _move(self )  : 
        if not self.out_stack : 
            while self.in_stack : 
                self.out_stack.append( self.in_stack.pop()) 

                
