class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

"""
so yeah i had a bit of rough time with this exercise  because of two lines i forgot , return head , i didn't think they were important 
, i thought we are using the class method (self) that's why i thought i didn't need to return it so the computer update the list  and that's a new lesson that i learned 
if using class method like (self) you don't need to return cause it is updating the actual linked list , but if not you have to return  so you tell the computer that we changed 
something or we added a new node , feeling bad that i asked chatgpt about what iam wrong about , but feeling happy that i learned new thing

what i've learned :
using self.head in class method -----> don't need to return the head
standalone function -----> if list is empty ----> need to return the head
standalone function -----> if list is not empty ----> can do both but recommended to do it

standalone function : A standalone function is a function that is not part of a class.
"""

def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
        return head

    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = SinglyLinkedListNode(data)
        return head