class Stack :
    def __init__(self):
        self.item = [ ]
        
    def is_empty(self):
        return len(self.item) == 0 
    
    def push(self , data):
        self.item.append(data)
        
    def pop(self) :
        if not self.is_empty():
            
            return self.item.pop()
        
        else : 
            raise IndexError ("stack is empty" )
        
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        
        else :
            raise IndentationError ("stack is empty")
        
        
    def size(self) :
        
        len(self.item)


s1 = Stack()
s1.push(30)      
s1.push(20)
s1.push(50)
s1.push(80)
s1.push(90)

print("top elements" , s1.peek())
print("remove elemetns" , s1.pop())

print("top elements" , s1.peek())
    