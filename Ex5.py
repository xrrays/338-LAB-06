# 

import heapq
import random
import timeit

class ListNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class SortedLinkedListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        new_node = ListNode(value, priority)
        if not self.head or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and priority >= current.next.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        if not self.heap:
            return None
        priority, value = heapq.heappop(self.heap)
        return value

def generate_random_tasks(n):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(1, 100)))
        else:
            tasks.append(('dequeue', None))
    return tasks

def measure_execution_time(priority_queue_class, tasks):
    pq = priority_queue_class()
    start_time = timeit.default_timer()
    for operation, value in tasks:
        if operation == 'enqueue':
            pq.enqueue(value, value)
        elif operation == 'dequeue':
            pq.dequeue()
    end_time = timeit.default_timer()
    overall_time = end_time - start_time
    average_time_per_operation = overall_time / len(tasks)
    return overall_time, average_time_per_operation

random_tasks = generate_random_tasks(1000)

linked_list_pq_time, linked_list_pq_avg_time = measure_execution_time(SortedLinkedListPriorityQueue, random_tasks)

heap_pq_time, heap_pq_avg_time = measure_execution_time(HeapPriorityQueue, random_tasks)

print(f"Overall Time for Sorted Linked List Prio Q: {linked_list_pq_time:.6f}")
print(f"Average Time: {linked_list_pq_avg_time:.6f}\n")

print(f"Overall Time for Priority Queue Heap: {heap_pq_time:.6f}")
print(f"Average Time: {heap_pq_avg_time:.6f}")


# The heap priority queue will orobably be faster since it is O(logn) time complexity whereas the enqueue operation can be as slow as O(n) for sorted linked lists.
