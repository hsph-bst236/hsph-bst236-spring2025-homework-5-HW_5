import pytest
from problem2 import Numeria_delta
import time

@pytest.mark.timeout(120)  # Set timeout to 2 minutes
def test_problem1():
    truth = 0.062  # This not real truth but the approximate value
    start_time = time.time()
    result = Numeria_delta()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n=== RESULT SUMMARY ===")
    print(f"Result value from Numeria_delta(): {result}")
    print(f"Execution time for Numeria_delta(): {execution_time:.4f} seconds")
    print(f"=== END SUMMARY ===\n")
    assert abs(result - truth) < 0.001, f"Result is not close to the expected truth"

if __name__ == "__main__":
    pytest.main() 