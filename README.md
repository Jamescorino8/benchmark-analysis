# benchmark-analysis

A Python project for benchmarking and analyzing the performance of common sorting and searching algorithms. It measures execution times across varying input sizes, then generates visualizations to compare algorithm efficiency.

## Setup

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jamescorino/benchmark-analysis.git
   cd benchmark-analysis
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. Install dependencies:

   ```bash
   pip install matplotlib
   ```

## Usage

Run the benchmark to collect timing data:

```bash
python benchmark.py
```

This generates `results.csv` with timing results for each algorithm, input size, and data distribution.

Then generate the performance plots:

```bash
python analysis.py
```

Output PNG files are written to the current directory (e.g. `plot_random.png`, `plot_sorted.png`).
