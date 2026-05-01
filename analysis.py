import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def load_results(filename="results.csv"):
    results = []
    with open(filename, newline="") as f:
        for row in csv.DictReader(f):
            results.append({
                "algorithm":    row["algorithm"],
                "input_size":   int(row["input_size"]),
                "distribution": row["distribution"],
                "elapsed_time": float(row["elapsed_time"]),
            })
    return results


def plot_by_distribution(results):
    # data[distribution][algorithm] = [(size, time), ...]
    data = defaultdict(lambda: defaultdict(list))
    for row in results:
        data[row["distribution"]][row["algorithm"]].append(
            (row["input_size"], row["elapsed_time"])
        )

    for dist in ["random", "sorted", "reverse-sorted"]:
        fig, ax = plt.subplots()

        for algorithm, points in sorted(data[dist].items()):
            points.sort()
            sizes = [p[0] for p in points]
            times = [p[1] for p in points]
            ax.plot(sizes, times, marker="o", label=algorithm)

        ax.set_title(f"Runtime vs Input Size ({dist})")
        ax.set_xlabel("Input Size")
        ax.set_ylabel("Elapsed Time (seconds)")
        ax.legend()
        ax.grid(True)

        fname = f"plot_{dist.replace('-', '_')}.png"
        fig.savefig(fname)
        plt.close(fig)
        print(f"Saved {fname}")


def plot_overlay(results, algorithm="merge_sort"):
    # One algorithm, one line per distribution
    data = defaultdict(list)
    for row in results:
        if row["algorithm"] == algorithm:
            data[row["distribution"]].append(
                (row["input_size"], row["elapsed_time"])
            )

    fig, ax = plt.subplots()

    for dist, points in sorted(data.items()):
        points.sort()
        sizes = [p[0] for p in points]
        times = [p[1] for p in points]
        ax.plot(sizes, times, marker="o", label=dist)

    ax.set_title(f"{algorithm} — Runtime by Distribution")
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Elapsed Time (seconds)")
    ax.legend()
    ax.grid(True)

    fname = f"plot_overlay_{algorithm}.png"
    fig.savefig(fname)
    plt.close(fig)
    print(f"Saved {fname}")


if __name__ == "__main__":
    results = load_results()
    plot_by_distribution(results)
    plot_overlay(results, algorithm="merge_sort")
