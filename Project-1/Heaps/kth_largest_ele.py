import heapq

def kth_largest_element(nums, k):
    # Convert the first k elements to a max heap
    max_heap = nums[:k]
    heapq.heapify(max_heap)

    # Process the remaining elements
    for num in nums[k:]:
        if num > max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, num)

    return max_heap[0]

# Example usage
nums = [3, 1, 4, 2, 5]
k = 2
kth_largest = kth_largest_element(nums, k)
print(f"The {k}th largest element is: {kth_largest}")
