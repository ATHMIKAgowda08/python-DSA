import time
def linear_time(n):
    print(f"\n0(n) for n = {n}")
    start = time.time()
    for i in range(n):
        pass  # Simulating O(n) operation
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

linear_time(10000)
linear_time(2000900)
linear_time(50000)

