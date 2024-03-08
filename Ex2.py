# Q1, Q2

import timeit
import random

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
    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)
    return root

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

def build_tree(data):
    root = None
    for item in data:
        root = insert(item, root)
    return root

def measure_search_performance(tree_root, data):
    total_time = 0
    for item in data:
        search_time = timeit.timeit(lambda: search(item, tree_root), number=10)
        total_time += search_time
    average_time = total_time / len(data)
    return average_time, total_time

sorted_vector = list(range(10000))
random.shuffle(sorted_vector)

tree_root = build_tree(sorted_vector)

average_time, total_time = measure_search_performance(tree_root, sorted_vector)
print("Average search time:", average_time)
print("Total search time:", total_time)


# Q3
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def measure_binary_search_performance(data):
    total_time = 0
    for item in data:
        search_time = timeit.timeit(lambda: binary_search(data, item), number=10)
        total_time += search_time
    average_time = total_time / len(data)
    return average_time, total_time

sorted_vector = list(range(10000))
random.shuffle(sorted_vector)

sorted_vector.sort()

average_time_bs, total_time_bs = measure_binary_search_performance(sorted_vector)
print("Average binary search time:", average_time_bs)
print("Total binary search time:", total_time_bs)



#4 ) The first method is faster, because the binary search tree is using trees instead of arrays to store it's data.
# Using trees instead of arrays is more efficient and can lead to lower complexity, as evidenced by the search times.