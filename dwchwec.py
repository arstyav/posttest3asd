class Node:
    def __init__(self, data):
    self.data = data
se  lf.next = None

class LinkedList:
    def __init__(self):
    self.head = None

def append(self, data):
    new_node = Node(data)

    if not self.head:
    self.head = new_node
    return

current_node = self.head
while current_node.next:
current_node = current_node.next

current_node.next = new_node

def insert(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

def delete(self, data):
    if not self.head:
    return

    if self.head.data == data:
    self.head = self.head.next
    return

current_node = self.head
while current_node.next:
    if current_node.next.data == data:
    current_node.next = current_node.next.next
    return
    current_node = current_node.next

def display(self):
    node_list = []
current_node = self.head

while current_node:
    node_list.append(current_node.data)
current_node = current_node.next

print(node_list)