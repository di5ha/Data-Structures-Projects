class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._heapify_down(0)

        return max_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Example usage
heap = MaxHeap()
heap.insert(10)
heap.insert(30)
heap.insert(20)
heap.insert(5)
heap.insert(15)

print("Max heap:")
print(heap.heap)

max_value = heap.delete_max()
print(f"Deleted max value: {max_value}")
print("Max heap after deletion:")
print(heap.heap)
