import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Quicksort Implementation

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort Implementation

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Performance Analysis - Time Complexity Demonstration

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Generate test cases
sizes = [100, 500, 1000, 5000, 10000]
results_deterministic = []
results_randomized = []

def generate_data(size, data_type):
    if data_type == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reverse_sorted":
        return list(range(size, 0, -1))

# Run empirical tests on different input distributions
for size in sizes:
    data_random = generate_data(size, "random")
    data_sorted = generate_data(size, "sorted")
    data_reverse_sorted = generate_data(size, "reverse_sorted")
    
    time_det_random = measure_time(quicksort, data_random[:])
    time_det_sorted = measure_time(quicksort, data_sorted[:])
    time_det_reverse = measure_time(quicksort, data_reverse_sorted[:])
    
    time_rand_random = measure_time(randomized_quicksort, data_random[:])
    time_rand_sorted = measure_time(randomized_quicksort, data_sorted[:])
    time_rand_reverse = measure_time(randomized_quicksort, data_reverse_sorted[:])
    
    results_deterministic.append((time_det_random, time_det_sorted, time_det_reverse))
    results_randomized.append((time_rand_random, time_rand_sorted, time_rand_reverse))

# Visualization
sizes_np = np.array(sizes)
results_deterministic_np = np.array(results_deterministic)
results_randomized_np = np.array(results_randomized)

plt.figure(figsize=(10, 6))
plt.plot(sizes_np, results_deterministic_np[:, 0], label="Deterministic - Random Data")
plt.plot(sizes_np, results_deterministic_np[:, 1], label="Deterministic - Sorted Data")
plt.plot(sizes_np, results_deterministic_np[:, 2], label="Deterministic - Reverse Sorted Data")
plt.plot(sizes_np, results_randomized_np[:, 0], label="Randomized - Random Data", linestyle='dashed')
plt.plot(sizes_np, results_randomized_np[:, 1], label="Randomized - Sorted Data", linestyle='dashed')
plt.plot(sizes_np, results_randomized_np[:, 2], label="Randomized - Reverse Sorted Data", linestyle='dashed')
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Comparison of Quicksort Implementations")
plt.legend()
plt.grid()
plt.show()
