"""
Queue Data Structure

Time Complexity:
- Enqueue: O(1) - add element to rear
- Dequeue: O(1) - remove element from front
- Front: O(1) - view front element
- Rear: O(1) - view rear element
- Is Empty: O(1) - check if queue is empty
- Size: O(1) - get number of elements

Space Complexity: O(n) - stores n elements

Description:
Queue is a linear data structure that follows the FIFO (First In First Out)
principle. Elements are added at the rear and removed from the front.
Common operations are enqueue (add), dequeue (remove), and peek (view front element).
"""

class Queue:
    """
    Queue implementation using Python list
    
    Operations:
    - enqueue(item): Add element to rear - O(1)
    - dequeue(): Remove and return front element - O(1)
    - front(): View front element without removing - O(1)
    - rear(): View rear element without removing - O(1)
    - is_empty(): Check if queue is empty - O(1)
    - size(): Get number of elements - O(1)
    - clear(): Remove all elements - O(1)
    """
    
    def __init__(self):
        """Initialize empty queue"""
        self._items = []
        self._size = 0
    
    def enqueue(self, item):
        """
        Add element to the rear of the queue
        
        Args:
            item: Element to be added
            
        Time Complexity: O(1)
        """
        self._items.append(item)
        self._size += 1
    
    def dequeue(self):
        """
        Remove and return the front element of the queue
        
        Returns:
            Front element of the queue
            
        Raises:
            IndexError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        self._size -= 1
        return self._items.pop(0)
    
    def front(self):
        """
        View the front element without removing it
        
        Returns:
            Front element of the queue
            
        Raises:
            IndexError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self._items[0]
    
    def rear(self):
        """
        View the rear element without removing it
        
        Returns:
            Rear element of the queue
            
        Raises:
            IndexError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if queue is empty
        
        Returns:
            bool: True if empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._size == 0
    
    def size(self):
        """
        Get the number of elements in the queue
        
        Returns:
            int: Number of elements
            
        Time Complexity: O(1)
        """
        return self._size
    
    def clear(self):
        """
        Remove all elements from the queue
        
        Time Complexity: O(1)
        """
        self._items.clear()
        self._size = 0
    
    def to_list(self):
        """
        Convert queue to Python list (front to rear)
        
        Returns:
            list: List representation of queue
            
        Time Complexity: O(n)
        """
        return self._items.copy()
    
    def copy(self):
        """
        Create a shallow copy of the queue
        
        Returns:
            Queue: New queue with same elements
            
        Time Complexity: O(n)
        """
        new_queue = Queue()
        new_queue._items = self._items.copy()
        new_queue._size = self._size
        return new_queue
    
    def __str__(self):
        """String representation of queue"""
        return f"Queue({self._items})"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        """Iterator for queue (front to rear)"""
        return iter(self._items)


class CircularQueue:
    """
    Circular Queue implementation using fixed-size array
    
    Advantages:
    - Efficient memory usage
    - No need to shift elements when dequeueing
    - True O(1) dequeue operation
    """
    
    def __init__(self, capacity):
        """
        Initialize circular queue with fixed capacity
        
        Args:
            capacity (int): Maximum number of elements
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self.capacity = capacity
        self._items = [None] * capacity
        self.front = 0
        self.rear = -1
        self._size = 0
    
    def enqueue(self, item):
        """
        Add element to the rear of the queue
        
        Time Complexity: O(1)
        """
        if self.is_full():
            raise OverflowError("Queue is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self._items[self.rear] = item
        self._size += 1
    
    def dequeue(self):
        """
        Remove and return the front element of the queue
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self._items[self.front]
        self._items[self.front] = None  # Optional: clear the slot
        self.front = (self.front + 1) % self.capacity
        self._size -= 1
        return item
    
    def front_element(self):
        """
        View the front element without removing it
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self._items[self.front]
    
    def rear_element(self):
        """
        View the rear element without removing it
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self._items[self.rear]
    
    def is_empty(self):
        """Check if queue is empty"""
        return self._size == 0
    
    def is_full(self):
        """Check if queue is full"""
        return self._size == self.capacity
    
    def size(self):
        """Get the number of elements"""
        return self._size
    
    def clear(self):
        """Remove all elements"""
        self._items = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self._size = 0
    
    def to_list(self):
        """Convert queue to Python list"""
        result = []
        for i in range(self._size):
            index = (self.front + i) % self.capacity
            result.append(self._items[index])
        return result
    
    def __str__(self):
        return f"CircularQueue({self.to_list()})"
    
    def __len__(self):
        return self._size


class LinkedListQueue:
    """
    Queue implementation using linked list
    
    Advantages:
    - No size limitation
    - Consistent O(1) operations
    - No need for resizing
    """
    
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        """Initialize empty queue"""
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, item):
        """
        Add element to the rear of the queue
        
        Time Complexity: O(1)
        """
        new_node = self.QueueNode(item)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1
    
    def dequeue(self):
        """
        Remove and return the front element of the queue
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        self._size -= 1
        return data
    
    def front_element(self):
        """
        View the front element without removing it
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self.front.data
    
    def rear_element(self):
        """
        View the rear element without removing it
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self.rear.data
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front is None
    
    def size(self):
        """Get the number of elements"""
        return self._size
    
    def clear(self):
        """Remove all elements"""
        self.front = None
        self.rear = None
        self._size = 0
    
    def to_list(self):
        """Convert queue to Python list"""
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self):
        return f"LinkedListQueue({self.to_list()})"
    
    def __len__(self):
        return self._size


def queue_analysis():
    """
    Provides complexity analysis for Queue data structure
    """
    return {
        'data_structure': 'Queue',
        'principle': 'FIFO (First In First Out)',
        'space_complexity': 'O(n)',
        'operations': {
            'enqueue': 'O(1)',
            'dequeue': 'O(1)',
            'front': 'O(1)',
            'rear': 'O(1)',
            'is_empty': 'O(1)',
            'size': 'O(1)',
            'clear': 'O(1)'
        },
        'applications': [
            'Task scheduling',
            'Print queue management',
            'Breadth-first search',
            'Message queues',
            'Buffer management',
            'Call center systems'
        ],
        'advantages': [
            'Fair ordering',
            'Constant time operations',
            'Memory efficient',
            'Predictable behavior'
        ],
        'disadvantages': [
            'Limited access (only front and rear)',
            'No random access',
            'Fixed maximum size in array implementation'
        ]
    }


def josephus_problem(n, k):
    """
    Solve Josephus problem using queue
    
    Args:
        n (int): Number of people
        k (int): Step size (every k-th person is eliminated)
        
    Returns:
        int: Position of survivor
    """
    queue = Queue()
    
    # Initialize queue with people numbered 1 to n
    for i in range(1, n + 1):
        queue.enqueue(i)
    
    # Simulate elimination process
    while queue.size() > 1:
        # Move k-1 people from front to rear
        for _ in range(k - 1):
            queue.enqueue(queue.dequeue())
        
        # Eliminate k-th person
        queue.dequeue()
    
    return queue.dequeue()


def reverse_queue(queue):
    """
    Reverse a queue using stack
    
    Args:
        queue: Queue to be reversed
        
    Returns:
        Queue: Reversed queue
    """
    from .stack import Stack
    
    stack = Stack()
    result = Queue()
    
    # Move all elements from queue to stack
    while not queue.is_empty():
        stack.push(queue.dequeue())
    
    # Move all elements from stack to result queue
    while not stack.is_empty():
        result.enqueue(stack.pop())
    
    return result


# Example usage and testing
if __name__ == "__main__":
    # Test array-based queue
    print("=== Array-based Queue ===")
    queue = Queue()
    
    # Test enqueue
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"After enqueues: {queue}")
    print(f"Size: {queue.size()}")
    
    # Test front and rear
    print(f"Front: {queue.front()}")
    print(f"Rear: {queue.rear()}")
    
    # Test dequeue
    dequeued = queue.dequeue()
    print(f"Dequeued: {dequeued}")
    print(f"After dequeue: {queue}")
    
    # Test iteration
    print("Iterating through queue:")
    for item in queue:
        print(f"  {item}")
    
    # Test circular queue
    print("\n=== Circular Queue ===")
    circular_queue = CircularQueue(3)
    circular_queue.enqueue('A')
    circular_queue.enqueue('B')
    circular_queue.enqueue('C')
    print(f"Circular queue: {circular_queue}")
    print(f"Is full: {circular_queue.is_full()}")
    
    dequeued = circular_queue.dequeue()
    print(f"Dequeued: {dequeued}")
    print(f"After dequeue: {circular_queue}")
    
    circular_queue.enqueue('D')
    print(f"After enqueue 'D': {circular_queue}")
    
    # Test linked list queue
    print("\n=== Linked List Queue ===")
    ll_queue = LinkedListQueue()
    ll_queue.enqueue('X')
    ll_queue.enqueue('Y')
    ll_queue.enqueue('Z')
    print(f"Linked list queue: {ll_queue}")
    print(f"Dequeued: {ll_queue.dequeue()}")
    
    # Test applications
    print("\n=== Queue Applications ===")
    
    # Josephus problem
    survivor = josephus_problem(7, 3)
    print(f"Josephus problem (n=7, k=3): Survivor is at position {survivor}")
    
    # Queue reversal
    original_queue = Queue()
    for i in range(1, 6):
        original_queue.enqueue(i)
    print(f"Original queue: {original_queue}")
    
    reversed_queue = reverse_queue(original_queue.copy())
    print(f"Reversed queue: {reversed_queue}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = queue_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
