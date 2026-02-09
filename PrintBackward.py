class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

"""
So yeah i used a stack to do is cause it's much easier , you just have to push your elements.data and then pop them , it didn't work for me the first
time cause i did a wrong condition where i wrote while llist.next in not None instead of  while llist is not None 
"""

def reversePrint(llist):
    sui = stack()
    if llist is None:
        return
    else:
        while llist is not None:
            sui.push(llist.data)
            llist = llist.next
    while sui.size() != 0:
        print(sui.pop())