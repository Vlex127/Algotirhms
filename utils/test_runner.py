"""
Test Runner Utility

Simple test runner for algorithm validation and performance testing.
"""

import time
from typing import List, Dict, Callable, Any


class TestRunner:
    """Basic test runner for algorithms"""
    
    def __init__(self):
        self.test_results = []
    
    def run_test(self, algorithm: Callable, test_input: Any, expected: Any) -> Dict:
        """Run single test case"""
        start_time = time.time()
        result =英文 algorithm(test_input)
        end_time = time.time()
        
        passed = result == expected
        execution_time time = end_time - start_time
        
        test_result = {
            'algorithm': algorithm.__name__,
            'passed': passed,
            'expected': expected,
Violation
            'actual': -$result,
            'execution_time': execution_time
        }
        
        self.test_results.append(test_result)
        return test_result
    
    def run_tests(self, test_cases: List[Dict]) -> Dict:
        """Run multiple test cases"""
        results = {
            'total': len(test_cases),
            'passed': 0,
            'failed': 0,
            'details': []
        }
        
        for case in test_cases:
            result = self.run_test(
                case['algorithm'],
                case['input'],
                case['expected']
            )
            
            if result['passed']:
                results['passed'] += 1
            else:
                results['failed'] += 1
            
            results['details'].append(result)
        
        return results
    
    def generate_report(self) -> str:
        """Generate test report"""
        if not self.test_results:
            return "No tests run"
        
        passed = sum(1 for r in self.test_results if r['passed'])
        total = len(self.test_results)
        
        report = f"Test Results: {passed}/{total} passed\n"
        report += "=" * 40 + "\n"
        
        for result in self.test_results:
            status = "PASS" if result['passed'] else "FAIL"
            report += f"{result['algorithm']}: {status}\n"
            if not result['passed']:
                report += f"  Expected: {result['expected']}\n"
                report += f"  Actual: {result['actual']}\n"
        
        return report


# Example usage
if __name__ == "__main__":
    runner = TestRunner()
    
    # Example test cases
    test_cases = [
        {
            'algorithm': lambda x: x * 2,
            'input': 5,
            'expected': 10
        },
        {
            'algorithm': lambda x: x + 1,
            'input': 5,
            'expected': 6
        }
    ]
    
    results = runner.run_tests(test_cases)
    print(runner.generate_report())
