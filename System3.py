class MaxHeap:
    def __init__(self):
        """Class to represent a MaxHeap"""

        self.heap = [] # Initialize an empty list to store heap elements.
        self.steps = 0 # Step counter.

    # Function to add new posts:
    def add_post(self, post):
        self.heap.append(post) # Appends items(posts).
        self.move_up(len(self.heap) - 1) # Restore the heap property by moving the newly added item up to its correct position.

    # Function to retrieve maximum:
    def retrieve_max(self):
        if len(self.heap) == 0: # If the heap is empty, return None.
            return None
        if len(self.heap) == 1: # If there is only one item in the heap, pop it.
            return self.heap.pop()

        # Save the maximum value (root).
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop() # Replace the root with the last item in the heap.
        self.move_down(0) # Restore the heap property by moving the new root down to its correct position.
        # Return the maximum value
        return max_val

    # Function to move the element up the heap until it's in the correct position:
    def move_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] <= self.heap[parent_index]: # If the parent is greater than or equal to the current element, stop.
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] # Swap the current element with its parent.
            index = parent_index # Move up to the parent index
            self.steps += 1  # Increment step counter

    # Function to move the element down the heap until it's in the correct position:
    def move_down(self, index):
        while index < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            max_index = index

            # Find the index of the maximum child
            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[max_index]:
                max_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[max_index]:
                max_index = right_child_index

            if max_index == index:# If the current element is already larger than its children, stop.
                break

            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index] # Swap the current element with its maximum child.
            index = max_index # Move down to the maximum child index
            self.steps += 1  # Increment step counter

    # Function to get the maximum value (root) of the heap:
    def get_max(self):
        return self.heap[0] if self.heap else None

    # Function to get the number of elements in the heap:
    def size(self):
        # Return the number of elements in the heap
        return len(self.heap)

# Test cases:
max_heap = MaxHeap()
# Insert posts with their view counts
max_heap.add_post(10000)
max_heap.add_post(2000)
max_heap.add_post(5000000)


# Retrieve the post with the most views:
most_viewed_post = max_heap.retrieve_max()
print("Most viewed post:", most_viewed_post)
print("Steps taken:", max_heap.steps)