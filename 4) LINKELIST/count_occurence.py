class Node :
    def __init__(self ,data):
        self.data = data
        self.next = None

def count_occurence(head , key):
    count = 0 
    current = head
    
    while current is not None :
        if current.data == key :
            count +=1
            
            
        current = current.next
    return count 


head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)

print(count_occurence(head , 1))
