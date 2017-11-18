import queue
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
        
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
        
    def pre_order(self):
        print(self.value,end=' ')
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.value,end=' ')
        if self.right_child:
            self.right_child.in_order()
            
    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.value,end=' ')
        
    def bfs(self):
        q = queue.Queue()
        q.put(self)
        while not q.empty():
            current_node = q.get()
            print(current_node.value,end=' ')
            if current_node.left_child:
                q.put(current_node.left_child)
            if current_node.right_child:
                q.put(current_node.right_child)

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')
b_node = a_node.left_child
b_node.insert_left('d')
b_node.insert_right('e')
c_node = a_node.right_child
c_node.insert_left('f')
c_node.insert_right('g')

"""
        a
    b       c
  d   e   f   g
"""

a_node.pre_order() #a b d e c f g
print()
a_node.in_order() #d b e a f c g
print()
a_node.post_order() #d e b f g c a
print()
a_node.bfs() #a b c d e f g
print()
