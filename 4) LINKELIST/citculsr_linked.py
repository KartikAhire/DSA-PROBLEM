class Node :
    def __init__(self ,data):
        self.data = data
        self.next = None


def circular_linked(head):
    if head is None :
        return 
    
    current = head 
    
    while True :
        print(current.data)
        
        
        current = current.next