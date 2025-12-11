"""
Documentation Generator

Generates comprehensive documentation for algorithms including
complexity analysis, usage examples, and performance metrics.
"""

import os
from typing import Dict, List, Any


class DocumentationGenerator:
    """Generates documentation for algorithm repository"""
    
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.modules = []
        self.algorithms = {}
    
    def scan_repository(self):
        """Scan repository for algorithms and modules"""
        modules = ['sorting', 'searching', 'data_structures', 
                  'graph_algorithms', 'dynamic_programming', 'greedy', 'divide_and_conquer']
        
        for module in modules:
            module_path = os.path.join(self.repo_path, module)
            if os.path.exists(module_path):
                self.modules.append(module)
                self.algorithms[module] = self._scan_module(module_path)
    
    def _scan_module(self, module_path: str) -> List[str]:
        """Scan module for algorithm files"""
        algorithms = []
        if os.path.exists(module_path):
            for file in os.listdir(module_path):
                if file.endswith('.py') and file != '__init__.py':
                    algorithms.append(file[:-3])  # Remove .py extension
        return algorithms
    
    def generate_readme(self) -> str:
        """Generate comprehensive README"""
        readme = """# Algorithms Repository

A comprehensive collection of algorithms implemented in Python with detailed
complexity analysis, examples, and testing utilities.

## Structure

"""
        
        for module in self.modules:
            readme += f"### {module.replace('_', ' ').title()}\n\n"
            algorithms = self.algorithms.get(module, [])
            for algo in algorithms:
                readme += f"- `{algo}`\n"
            readme += "\n"
        
        readme += """## Usage

```python
from sorting.bubble_sort import bubble_sort
from data_structures.stack import Stack

# Use algorithms
sorted_array = bubble_sort([5, 2, 8, 1, 9])
stack = Stack()
stack.push(10)
```

## Complexity Analysis

Each algorithm includes detailed time and space complexity analysis
along with performance comparisons and optimization techniques.

## Testing

Run tests using the main.py script:

```bash
python main.py --test
```
"""
        return readme
    
    def generate_algorithm_docs(self, algorithm_name: str) -> str:
        """Generate documentation for specific algorithm"""
        return f"""
# {algorithm_name}

## Description
[Algorithm description here]

## Complexity
- Time: O(n)
- Space: O(n)

## Usage
```python
# Example usage
```
"""
    
    def save_documentation(self, output_dir: str):
        """Save generated documentation to files"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate README
        readme_content = self.generate_readme()
        with open(os.path.join(output_dir, 'README.md'), 'w') as f:
            f.write(readme_content)
        
        # Generate individual algorithm docs
        for module, algorithms in self.algorithms.items():
            for algo in algorithms:
                doc_content = self.generate_algorithm_docs(algo)
                doc_path = os.path.join(output_dir, f"{algo}.md")
                with open(doc_path, 'w') as f:
                    f.write(doc_content)


if __name__ == "__main__":
    # Example usage
    generator = DocumentationGenerator(".")
    generator.scan_repository()
    generator.save_documentation("./docs/output")
    print("Documentation generated successfully!")
