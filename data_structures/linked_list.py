"""
Linked List Data Structure

Time Complexity:
- Access: O(n) - need to traverse from head
- Search: O(n) - need to traverse to find element
- Insertion: O(1) at beginning, O(n) at end/middle
- Deletion: O(1) at beginning, O(n) at end/middle

Space Complexity: O(n) - stores n elements plus n pointers

Description:
A linked list is a linear data structure where elements are not stored at
contiguous memory locations. Each element (node) contains data and a pointer
to the next node in the sequence.
"""

class Node:
    """
    Node class for Linked List
    
    Attributes:
        data: The data stored in the node
        next: Reference to the next node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """
    Singly Linked List implementation
    
    Operations:
    - append(data): Add element to end - O(n)
    - prepend(data): Add element to beginning - O(1)
    - insert(data, position): Insert at specific position - O(n)
    - delete(data): Remove first occurrence - O(n)
    - search(data): Find element - O(n)
    - get_at(index): Get element at index - O(n)
    - size(): Get number of elements - O(1)
    - is_empty(): Check if empty - O(1)
    """
    
    def __init__(self):
        """Initialize empty linked list"""
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        """
        Add element to the end of the linked list
        
        Args:
            data: Data to be added
            
        Time Complexity: O(n) - need to traverse to end
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, data):
        """
        Add element to the beginning of the linked list
        
        Args:
            data: Data to be added
            
        Time Complexity: O(1) - direct insertion at head
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, data, position):
        """
        Insert element at specific position
        
        Args:
            data: Data to be inserted
            position (int): Position where to insert (0-based)
            
        Time Complexity: O(n) - need to traverse to position
        """
        if position < 0 or position > self._size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            self.prepend(data)
        elif position == self._size:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            
            # Traverse to position before insertion point
            for _ in range(position - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            self._size += 1
    
    def delete(self, data):
        """
        Delete first occurrence of data from linked list
        
        Args:
            data: Data to be deleted
            
        Returns:
            bool: True if deleted, False if not found
            
        Time Complexity: O(n) - need to traverse to find element
        """
        if self.is_empty():
            return False
        
        # Special case: head node
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next is None:
            return False  # Data not found
        
        # Remove node
        current.next = current.next.next
        
        # Update tail if necessary
        if current.next is None:
            self.tail = current
        
        self._size -= 1
        return True
    
    def delete_at(self, position):
        """
        Delete element at specific position
        
        Args:
            position (int): Position of element to delete (0-based)
            
        Returns:
            Data of deleted element
            
        Time Complexity: O(n) - need to traverse to position
        """
        if position < 0 or position >= self._size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            
            data = current.next.data
            current.next = current.next.next
            
            if current.next is None:
                self.tail = current
        
        self._size -= 1
        return data
    
    def search(self, data):
        """
        Search for data in linked list
        
        Args:
            data: Data to search for
            
        Returns:
            int: Index of first occurrence, -1 if not found
            
        Time Complexity: O(n) - need to traverse
        """
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get_at(self, index):
        """
        Get element at specific index
        
        Args:
            index (int): Index of element to retrieve
            
        Returns:
            Data at specified index
            
        Time Complexity: O(n) - need to traverse to index
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def update_at(self, index, data):
        """
        Update element at specific index
        
        Args:
            index (int): Index of element to update
            data: New data value
            
        Time Complexity: O(n) - need to traverse to index
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        current.data = data
    
    def size(self):
        """
        Get size of linked list
        
        Returns:
            int: Number of elements in linked list
            
        Time Complexity: O(1) - stored as attribute
        """
        return self._size
    
    def is_empty(self):
        """
        Check if linked list is empty
        
        Returns:
            bool: True if empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self.head is None
    
    def clear(self):
        """
        Clear all elements from linked list
        
        Time Complexity: O(1)
        """
        self.head = None
        self.tail = None
        self._size = 0
    
    def to_list(self):
        """
        Convert linked list to Python list
        
        Returns:
            list: Python list containing all elements
            
        Time Complexity: O(n)
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def reverse(self):
        """
        Reverse the linked list in place
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        self.tail = current
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def __str__(self):
        """String representation of linked list"""
        elements = self.to_list()
        return f"LinkedList({elements})"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        """Iterator for linked list"""
        current = self.head
        while current:
            yield current.data
            current = current.next


class DoublyLinkedList:
    """
    Doubly Linked List implementation
    
    Each node has both next and previous pointers
    """
    
    class DoublyNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        """Add element to end - O(1)"""
        new_node = self.DoublyNode(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, data):
        """Add element to beginning - O(1)"""
        new_node = self.DoublyNode(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self._size += 1
    
    def delete(self, data):
        """Delete first occurrence - O(n)"""
        current = self.head
        
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def size(self):
        return self._size
    
    def is_empty(self):
        return self.head is None
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


def linked_list_analysis():
    """
    Provides complexity analysis for Linked List data structure
    """
    return {
        'data_structure': 'Linked List',
        'space_complexity': 'O(n)',
        'operations': {
            'access': 'O(n)',
            'search': 'O(n)',
            'insertion_front': 'O(1)',
            'insertion_end': 'O(n)',
            'insertion_middle': 'O(n)',
            'deletion_front': 'O(1)',
            'deletion_end': 'O(n)',
            'deletion_middle': 'O(n)'
        },
        'advantages': [
            'Dynamic size',
            'Efficient insertion/deletion at beginning',
            'No memory waste',
            'Easy insertion/deletion in middle after finding position'
        ],
        'disadvantages': [
            'Sequential access only',
            'Extra memory for pointers',
            'Not cache-friendly',
            'O(n) access time'
        ]
    }


# Example usage and testing
if __name__ == "__main__":
    # Test singly linked list
    print("=== Singly Linked List ===")
    ll = LinkedList()
    
    # Test append
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print(f"After append: {ll}")
    
    # Test prepend
    ll.prepend(5)
    print(f"After prepend: {ll}")
    
    # Test insert
    ll.insert(15, 2)
    print(f"After insert at position 2: {ll}")
    
    # Test search
    index = ll.search(20)
    print(f"Search for 20: found at index {index}")
    
    # Test get_at
    element = ll.get_at(2)
    print(f"Element at index 2: {element}")
    
    # Test delete
    ll.delete(15)
    print(f"After deleting 15: {ll}")
    
    # Test reverse
    ll.reverse()
    print(f"After reverse: {ll}")
    
    # Test iteration
    print("Iterating through list:")
    for item in ll:
        print(f"  {item}")
    
    # Test doubly linked list
    print("\n=== Doubly Linked List ===")
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print(f"Doubly linked list: {dll.to_list()}")
    
    dll.delete(2)
    print(f"After deleting 2: {dll.to_list()}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = linked_list_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
