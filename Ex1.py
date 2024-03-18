# Code from d2l and chatgpt

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)    
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return newnode

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

import timeit
from random import shuffle

########### METHOD 1 ##########################

# Assuming the Node and insert functions are defined as provided earlier

# Generate a sorted vector of 10000 elements
sorted_vector = list(range(10000))
shuffle(sorted_vector)  # Shuffle to simulate random insertion order

# Build the tree by inserting each element
root = None
for element in sorted_vector:
    root = insert(element, root)

# Define the search test function
def search_test():
    for element in range(10000):
        search(element, root)

# Time the search for each element, averaged across 10 tries
average_time = timeit.timeit('search_test()', globals=globals(), number=10) / 10000
total_time = timeit.timeit('search_test()', globals=globals(), number=10)

print(f"Average time per search using method 1: {average_time:.6f} seconds")
print(f"Total time for all searches using method 1: {total_time:.6f} seconds")

############## METHOD 2 ################################

# Assuming the Node, insert, and search functions are defined as provided earlier

# Generate a sorted vector of 10000 elements and shuffle it
sorted_vector = list(range(10000))
shuffle(sorted_vector)  # Shuffle to simulate random insertion order

# Build the tree by inserting each element
root = None
for element in sorted_vector:
    root = insert(element, root)

# Shuffle the vector again for the search test
shuffle(sorted_vector)

# Define the search test function
def search_test():
    for element in sorted_vector:
        search(element, root)

# Time the search for each element, averaged across 10 tries
average_time = timeit.timeit('search_test()', globals=globals(), number=10) / 10000
total_time = timeit.timeit('search_test()', globals=globals(), number=10)

print(f"Average time per search for method 2: {average_time:.6f} seconds")
print(f"Total time for all searches for method 2: {total_time:.6f} seconds")


# IThe second technique of evaluating search performance will be faster, which shuffles the vector twice before creating the binary search tree and one more before searching. 
# This is so that search paths can be shortened and search times can be accelerated. A randomly constructed tree has a higher probability of being balanced than one constructed from a sorted vector. 
# Longer search times are a result of the first approach, which inserts components in a sorted order and often results in an imbalanced tree that resembles a linked list.
# However, in the end it all depends on how lucky you were with getting a good vector.