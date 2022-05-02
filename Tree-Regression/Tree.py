'''
Module for holding Binary Tree
Desc: Binary Tree we use for storing results of tree regression
'''

import numpy as np

class Node:

    def __init__(self, x_elements, y_elements, values, x_min, x_max, y_min, y_max):
        self.x_elements = x_elements
        self.y_elements = y_elements
        self.vals = values
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
    
    def print_me(self):
        #print(self.x_elements)
        #print(self.y_elements)
        print(f"x:({self.x_min}, {self.x_max}); y:({self.y_min}, {self.y_max})")
        #print(self.vals)




'''
class BinaryTree:
    root: Node
    image: np.ndarray

    def __init__(self, root:Node):
        #do some cool stuff
        self.root = root
    
    def display_image(self, dim):
        image = np.zeros(dim)
        #traverse tree to display the image:
        #color in sections that are leaf nodes
        print("Do traversal here")
    
    def traverse_img(self, node: Node):
        #idea: if a region has None as a child, it si 
        #np.put()
        print("woah")

    def rec_print_tree(self, node: Node):
        print(f"Split: {node.split}; left color: {node.c1}; right color: {node.c2}")
        if (node.left != None):
            self.rec_print_tree(node.left)

        if (node.right != None):
            self.rec_print_tree(node.right)
    
    def print_tree(self):
        self.rec_print_tree(self.root)

        '''