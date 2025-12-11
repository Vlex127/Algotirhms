"""
Stack Data Structure

Time Complexity:
- Push: O(1) - add element to top
- Pop: O(1) - remove element from top
- Peek: O(1) - view top element
- Is Empty: O(1) - check if stack is empty
- Size: O(1) - get number of elements

Space Complexity: O(n) - stores n elements

Description:
Stack is a linear data structure that follows the LIFO (Last In First Out)
principle. Elements can only be added and removed from one end (the top).
Common operations are push (add), pop (remove), and peek (view top element).
"""

class Stack:
    """
    Stack implementation using Python list
    
    Operations:
    - push(item): Add element to top - O(1)
    - pop(): Remove and return top element - O(1)
    - peek(): View top element without removing - O(1)
    - is_empty(): Check if stack is empty - O(1)
    - size(): Get number of elements - O(1)
    - clear(): Remove all elements - O(1)
    """
    
    def __init__(self):
        """Initialize empty stack"""
        self._items = []
        self._size = 0
    
    def push(self, item):
        """
        Add element to the top of the stack
        
        Args:
            item: Element to be added
            
        Time Complexity: O(1)
        """
        self._items.append(item)
        self._size += 1
    
    def pop(self):
        """
        Remove and return the top element of the stack
        
        Returns:
            Top element of the stack
            
        Raises:
            IndexError: If stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        self._size -= 1
        return self._items.pop()
    
    def peek(self):
        """
        View the top element without removing it
        
        Returns:
            Top element of the stack
            
        Raises:
            IndexError: If stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if stack is empty
        
        Returns:
            bool: True if empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._size == 0
    
    def size(self):
        """
        Get the number of elements in the stack
        
        Returns:
            int: Number of elements
            
        Time Complexity: O(1)
        """
        return self._size
    
    def clear(self):
        """
        Remove all elements from the stack
        
        Time Complexity: O(1)
        """
        self._items.clear()
        self._size = 0
    
    def to_list(self):
        """
        Convert stack to Python list (top to bottom)
        
        Returns:
            list: List representation of stack
            
        Time Complexity: O(n)
        """
        return self._items.copy()
    
    def copy(self):
        """
        Create a shallow copy of the stack
        
        Returns:
            Stack: New stack with same elements
            
        Time Complexity: O(n)
        """
        new_stack = Stack()
        new_stack._items = self._items.copy()
        new_stack._size = self._size
        return new_stack
    
    def __str__(self):
        """String representation of stack"""
        return f"Stack({self._items})"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        """Iterator for stack (top to bottom)"""
        return iter(reversed(self._items))


class LinkedListStack:
    """
    Stack implementation using linked list
    
    Advantages over array-based stack:
    - No size limitation
    - Consistent O(1) operations regardless of implementation
    - No need for resizing
    """
    
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        """Initialize empty stack"""
        self.top = None
        self._size = 0
    
    def push(self, item):
        """
        Add element to the top of the stack
        
        Time Complexity: O(1)
        """
        new_node = self.StackNode(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        """
        Remove and return the top element of the stack
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data
    
    def peek(self):
        """
        View the top element without removing it
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.top.data
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None
    
    def size(self):
        """Get the number of elements"""
        return self._size
    
    def clear(self):
        """Remove all elements"""
        self.top = None
        self._size = 0
    
    def to_list(self):
        """Convert stack to Python list"""
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self):
        return f"LinkedListStack({self.to_list()})"
    
    def __len__(self):
        return self._size


def stack_analysis():
    """
    Provides complexity analysis for Stack data structure
    """
    return {
        'data_structure': 'Stack',
        'principle': 'LIFO (Last In First Out)',
        'space_complexity': 'O(n)',
        'operations': {
            'push': 'O(1)',
            'pop': 'O(1)',
            'peek': 'O(1)',
            'is_empty': 'O(1)',
            'size': 'O(1)',
            'clear': 'O(1)'
        },
        'applications': [
            'Function call stack',
            'Expression evaluation',
            'Undo/redo operations',
            'Backtracking algorithms',
            'Browser history',
            'Memory management'
        ],
        'advantages': [
            'Simple implementation',
            'Constant time operations',
            'Memory efficient',
            'Predictable behavior'
        ],
        'disadvantages': [
            'Limited access (only top element)',
            'No random access',
            'Fixed maximum size in array implementation'
        ]
    }


def is_balanced_parentheses(expression):
    """
    Check if parentheses are balanced using stack
    
    Args:
        expression (str): String containing parentheses
        
    Returns:
        bool: True if balanced, False otherwise
    """
    stack = Stack()
    opening = {'(', '[', '{'}
    closing = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != closing[char]:
                return False
    
    return stack.is_empty()


def evaluate_postfix(expression):
    """
    Evaluate postfix expression using stack
    
    Args:
        expression (str): Postfix expression (space-separated tokens)
        
    Returns:
        int/float: Result of evaluation
    """
    stack = Stack()
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(int(token))
        elif token.replace('.', '', 1).isdigit() or (token[0] == '-' and token[1:].replace('.', '', 1).isdigit()):
            stack.push(float(token))
        else:
            # Operator
            if stack.size() < 2:
                raise ValueError("Invalid expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
            elif token == '^':
                stack.push(a ** b)
            else:
                raise ValueError(f"Unknown operator: {token}")
    
    if stack.size() != 1:
        raise ValueError("Invalid expression")
    
    return stack.pop()


def reverse_string_stack(s):
    """
    Reverse a string using stack
    
    Args:
        s (str): String to reverse
        
    Returns:
        str: Reversed string
    """
    stack = Stack()
    
    # Push all characters
    for char in s:
        stack.push(char)
    
    # Pop to build reversed string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


# Example usage and testing
if __name__ == "__main__":
    # Test array-based stack
    print("=== Array-based Stack ===")
    stack = Stack()
    
    # Test push
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"After pushes: {stack}")
    print(f"Size: {stack.size()}")
    
    # Test peek
    print(f"Peek: {stack.peek()}")
    
    # Test pop
    popped = stack.pop()
    print(f"Popped: {popped}")
    print(f"After pop: {stack}")
    
    # Test iteration
    print("Iterating through stack:")
    for item in stack:
        print(f"  {item}")
    
    # Test linked list stack
    print("\n=== Linked List Stack ===")
    ll_stack = LinkedListStack()
    ll_stack.push('A')
    ll_stack.push('B')
    ll_stack.push('C')
    print(f"Linked list stack: {ll_stack}")
    print(f"Popped: {ll_stack.pop()}")
    
    # Test applications
    print("\n=== Stack Applications ===")
    
    # Balanced parentheses
    expressions = ["((a+b)*c)", "([{}])", "([)]", "((())"]
    for expr in expressions:
        balanced = is_balanced_parentheses(expr)
        print(f"'{expr}' is balanced: {balanced}")
    
    # Postfix evaluation
    postfix_expr = "3 4 + 2 * 7 /"
    result = evaluate_postfix(postfix_expr)
    print(f"Postfix '{postfix_expr}' = {result}")
    
    # String reversal
    original = "Hello, World!"
    reversed_str = reverse_string_stack(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_str}")
    
    # Print complexity analysis
    print("\nComplexity Analysis:")
    analysis = stack_analysis()
    for key, value in analysis.items():
        print(f"{key}: {value}")
