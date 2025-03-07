from problem1 import sig1_M
import pytest
import time

@pytest.mark.timeout(120)  # Set timeout to 2 minutes
def test_problem1():
    truth = 1.27 # This not real truth but the approximate value
    start_time = time.time()
    result = sig1_M()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n=== RESULT SUMMARY ===")
    print(f"Result value from sig1_M(): {result}")
    print(f"Execution time for sig1_M(): {execution_time:.4f} seconds")
    print(f"=== END SUMMARY ===\n")
    assert abs(result - truth) < 0.01, f"Result is not close to the expected truth"

if __name__ == "__main__":
    pytest.main() 