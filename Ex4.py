# chatgpt generated

class SimpleHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        print(f"Heapifying array: {arr}")
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)
        print(f"Heap after heapify: {self.heap}")

    def enqueue(self, element):
        print(f"Enqueueing: {element}")
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)
        print(f"Heap after enqueue: {self.heap}")

    def dequeue(self):
        print("Dequeuing...")
        if len(self.heap) == 0:
            print("Heap is empty, nothing to dequeue.")
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        print(f"Heap after dequeue: {self.heap}")
        return root

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def _sift_down(self, index):
        n = len(self.heap)
        while index < n:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

# Test Cases
import random

# Test 1: Input array is already a correctly sorted heap
heap = SimpleHeap()
test_array = [1, 2, 3, 4, 5, 6, 7]
heap.heapify(test_array)
assert heap.heap == [1, 2, 3, 4, 5, 6, 7]

# Test 2: Input array is empty
heap = SimpleHeap()
test_array = []
heap.heapify(test_array)
assert heap.heap == []

# Test 3: Input array is a long, randomly shuffled list of integers
heap = SimpleHeap()
test_array = list(range(100))
random.shuffle(test_array)
heap.heapify(test_array)
while heap.heap:
    removed = heap.dequeue()
    if heap.heap:
        assert removed <= heap.heap[0]

# Test 4: Starting with an array of length 10 and enqueueing until length 15
heap = SimpleHeap()
test_array = list(range(10))
random.shuffle(test_array)
heap.heapify(test_array)
print(f"Initial heap: {heap.heap}")

for i in range(10, 15):
    heap.enqueue(i)
    print(f"Heap after enqueueing {i}: {heap.heap}")
    # Check the heap property: every parent node is less than or equal to its child nodes
    assert all(heap.heap[i] <= heap.heap[2 * i + 1] for i in range((len(heap.heap) - 2) // 2 + 1) if 2 * i + 1 < len(heap.heap))
    assert all(heap.heap[i] <= heap.heap[2 * i + 2] for i in range((len(heap.heap) - 2) // 2 + 1) if 2 * i + 2 < len(heap.heap))

print("Test passed! The heap property is maintained after each enqueue operation.")


print("All tests passed!")


