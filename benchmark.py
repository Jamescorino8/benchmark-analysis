import time, random, csv
from algorithms import bubble_sort, insertion_sort, merge_sort, quicksort, linear_search, binary_search

def generate_array(size, distribution):
    arr = list(range(size))
    if distribution == "random":
        random.shuffle(arr)
    elif distribution == "reverse-sorted":
        arr.reverse()
    return arr

def timing(func, data, *args):
    start = time.perf_counter()
    func(data.copy(), *args)
    elapsed = time.perf_counter() - start
    return elapsed

def save_results(results, filename="results.csv"):
    fieldnames = ["algorithm", "input_size", "distribution", "elapsed_time"]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()       # writes the column name row
        writer.writerows(results)  # writes all the data rows at once

sorting_algorithms = [
    ("bubble_sort", bubble_sort),
    ("insertion_sort", insertion_sort),
    ("merge_sort", merge_sort),
    ("quicksort", quicksort),
]

search_algorithms = [
    ("linear_search", linear_search),
    ("binary_search", binary_search),
]

slow_sizes = [100, 500, 1000, 5000, 10000]       # O(n²) algorithms cap at 10k
all_sizes  = [100, 500, 1000, 5000, 10000, 50000]
distributions = ["random", "sorted", "reverse-sorted"]

results = []

for name, func in sorting_algorithms:
    sizes = slow_sizes if name in ("bubble_sort", "insertion_sort") else all_sizes
    for size in sizes:
        for dist in distributions:
            arr = generate_array(size, dist)
            elapsed = timing(func, arr)
            results.append({
                "algorithm": name,
                "input_size": size,
                "distribution": dist,
                "elapsed_time": elapsed,
            })

for name, func in search_algorithms:
    for size in all_sizes:
        for dist in distributions:
            arr = generate_array(size, dist)
            target = size // 2
            # binary_search requires a sorted array
            if name == "binary_search":
                arr = sorted(arr)
            elapsed = timing(func, arr, target)
            results.append({
                "algorithm": name,
                "input_size": size,
                "distribution": dist,
                "elapsed_time": elapsed,
            })

save_results(results)
print(f"Saved {len(results)} records to results.csv")
