"""
Matplotlib Testing Module

Provides visualization and testing capabilities for algorithm performance
using matplotlib for charts and graphs.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import time
from typing import List, Dict, Callable, Any, Tuple
import os


class MatplotlibTester:
    """Matplotlib-based testing and visualization for algorithms"""
    
    def __init__(self, output_dir: str = "test_results"):
        self.output_dir = output_dir
        self.test_results = []
        self.performance_data = {}
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def benchmark_algorithm(self, algorithm: Callable, input_sizes: List[int], 
                           generator: Callable = None) -> Dict:
        """
        Benchmark algorithm across different input sizes
        """
        if generator is None:
            generator = lambda n: list(range(n))  # Default: sequential data
        
        times = []
        results = []
        
        for size in input_sizes:
            # Generate test data
            test_data = generator(size)
            
            # Time the algorithm
            start_time = time.time()
            result = algorithm(test_data.copy())
            end_time = time.time()
            
            execution_time = end_time - start_time
            times.append(execution_time)
            results.append(result)
        
        return {
            'input_sizes': input_sizes,
            'execution_times': times,
            'results': results
        }
    
    def compare_algorithms(self, algorithms: Dict[str, Callable], 
                          input_sizes: List[int], 
                          generator: Callable = None) -> Dict:
        """
        Compare multiple algorithms performance
        """
        comparison_data = {}
        
        for name, algorithm in algorithms.items():
            print(f"Benchmarking {name}...")
            data = self.benchmark_algorithm(algorithm, input_sizes, generator)
            comparison_data[name] = data
        
        self.performance_data = comparison_data
        return comparison_data
    
    def plot_performance_comparison(self, title: str = "Algorithm Performance Comparison",
                                  save_path: str = None) -> str:
        """
        Create performance comparison plot
        """
        if not self.performance_data:
            raise ValueError("No performance data available. Run compare_algorithms first.")
        
        plt.figure(figsize=(12, 8))
        
        for name, data in self.performance_data.items():
            plt.plot(data['input_sizes'], data['execution_times'], 
                    marker='o', linewidth=2, label=name)
        
        plt.xlabel('Input Size')
        plt.ylabel('Execution Time (seconds)')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Save plot
        if save_path is None:
            save_path = os.path.join(self.output_dir, "performance_comparison.png")
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return save_path
    
    def plot_complexity_analysis(self, theoretical_complexities: Dict[str, str],
                                save_path: str = None) -> str:
        """
        Plot empirical vs theoretical complexity
        """
        if not self.performance_data:
            raise ValueError("No performance data available.")
        
        plt.figure(figsize=(14, 10))
        
        # Create subplots for different algorithm types
        algorithms = list(self.performance_data.keys())
        n_algorithms = len(algorithms)
        
        for i, name in enumerate(algorithms):
            plt.subplot(2, 2, i+1 if i < 4 else 4)
            
            data = self.performance_data[name]
            input_sizes = np.array(data['input_sizes'])
            times = np.array(data['execution_times'])
            
            # Plot empirical data
            plt.loglog(input_sizes, times, 'bo-', label='Empirical', linewidth=2)
            
            # Plot theoretical complexity if provided
            if name in theoretical_complexities:
                complexity = theoretical_complexities[name]
                if complexity == 'O(n^2)':
                    theoretical = input_sizes**2 / np.max(input_sizes**2) * np.max(times)
                elif complexity == 'O(n log n)':
                    theoretical = input_sizes * np.log(input_sizes) / np.max(input_sizes * np.log(input_sizes)) * np.max(times)
                elif complexity == 'O(n)':
                    theoretical = input_sizes / np.max(input_sizes) * np.max(times)
                elif complexity == 'O(log n)':
                    theoretical = np.log(input_sizes) / np.max(np.log(input_sizes)) * np.max(times)
                else:
                    theoretical = times  # Fallback
                
                plt.loglog(input_sizes, theoretical, 'r--', label='Theoretical', linewidth=2)
            
            plt.xlabel('Input Size')
            plt.ylabel('Time (seconds)')
            plt.title(f'{name} Complexity')
            plt.legend()
            plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path is None:
            save_path = os.path.join(self.output_dir, "complexity_analysis.png")
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return save_path
    
    def create_algorithm_heatmap(self, category_data: Dict[str, Dict], 
                                save_path: str = None) -> str:
        """
        Create heatmap showing algorithm performance across categories
        """
        categories = list(category_data.keys())
        algorithms = set()
        for cat_data in category_data.values():
            algorithms.update(cat_data.keys())
        algorithms = sorted(list(algorithms))
        
        # Create performance matrix
        performance_matrix = []
        for category in categories:
            row = []
            for algorithm in algorithms:
                if algorithm in category_data[category]:
                    # Use average time from last benchmark
                    times = category_data[category][algorithm]['execution_times']
                    avg_time = np.mean(times)
                    row.append(avg_time)
                else:
                    row.append(np.nan)  # Algorithm not in this category
            performance_matrix.append(row)
        
        performance_matrix = np.array(performance_matrix)
        
        # Create heatmap
        plt.figure(figsize=(12, 8))
        im = plt.imshow(performance_matrix, cmap='RdYlBu_r', aspect='auto')
        
        # Set ticks and labels
        plt.xticks(range(len(algorithms)), algorithms, rotation=45, ha='right')
        plt.yticks(range(len(categories)), categories)
        
        # Add colorbar
        cbar = plt.colorbar(im)
        cbar.set_label('Average Execution Time (seconds)')
        
        plt.title('Algorithm Performance Heatmap by Category')
        plt.tight_layout()
        
        if save_path is None:
            save_path = os.path.join(self.output_dir, "performance_heatmap.png")
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return save_path
    
    def generate_test_report(self, save_path: str = None) -> str:
        """
        Generate comprehensive test report with visualizations
        """
        report_lines = []
        report_lines.append("# Algorithm Performance Test Report")
        report_lines.append("=" * 50)
        report_lines.append("")
        
        # Performance summary
        if self.performance_data:
            report_lines.append("## Performance Summary")
            report_lines.append("")
            
            for name, data in self.performance_data.items():
                avg_time = np.mean(data['execution_times'])
                max_time = np.max(data['execution_times'])
                min_time = np.min(data['execution_times'])
                
                report_lines.append(f"### {name}")
                report_lines.append(f"- Average Time: {avg_time:.6f} seconds")
                report_lines.append(f"- Min Time: {min_time:.6f} seconds")
                report_lines.append(f"- Max Time: {max_time:.6f} seconds")
                report_lines.append(f"- Input Sizes: {data['input_sizes']}")
                report_lines.append("")
        
        # Generate visualizations
        if self.performance_data:
            try:
                perf_plot = self.plot_performance_comparison()
                report_lines.append(f"![Performance Comparison]({os.path.basename(perf_plot)})")
                report_lines.append("")
                
                complexity_plot = self.plot_complexity_analysis({})
                report_lines.append(f"![Complexity Analysis]({os.path.basename(complexity_plot)})")
                report_lines.append("")
            except Exception as e:
                report_lines.append(f"Error generating plots: {e}")
                report_lines.append("")
        
        # Save report
        report_text = "\n".join(report_lines)
        
        if save_path is None:
            save_path = os.path.join(self.output_dir, "test_report.md")
        
        with open(save_path, 'w') as f:
            f.write(report_text)
        
        return save_path


# Example usage and test functions
def test_sorting_algorithms():
    """Test sorting algorithms with matplotlib visualization"""
    from sorting.bubble_sort import bubble_sort
    from sorting.quick_sort import quick_sort
    from sorting.merge_sort import merge_sort
    
    tester = MatplotlibTester()
    
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Quick Sort': quick_sort,
        'Merge Sort': merge_sort
    }
    
    input_sizes = [10, 50, 100, 200, 500]
    
    # Compare algorithms
    comparison_data = tester.compare_algorithms(algorithms, input_sizes)
    
    # Generate visualizations
    tester.plot_performance_comparison("Sorting Algorithms Comparison")
    
    theoretical_complexities = {
        'Bubble Sort': 'O(n^2)',
        'Quick Sort': 'O(n log n)',
        'Merge Sort': 'O(n log n)'
    }
    
    tester.plot_complexity_analysis(theoretical_complexities)
    
    # Generate report
    report_path = tester.generate_test_report()
    print(f"Test report generated: {report_path}")
    
    return comparison_data


if __name__ == "__main__":
    # Run example test
    test_sorting_algorithms()
