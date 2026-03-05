# Programming Assignment 2: Greedy Algorithms

### Xabier Sienra (80213894)

### Hailey Pham (24752485)

# How to run code

### Requirements

Python 3 is required to run all of the assignment code. Depending on your device, 'python' may need to be replaced with 'py' or 'python3' in the following commands.

### Input Format

The program takes in as input a text file in the following format:

```
k m
r1 r2 r3 ... rm
```

where `k`, `m`, and each of the `ri`'s are space-separated integers, and:

- `k` >=1 is the cache capacity
- `m` is the number of requests
- `r1 r2 r3 ... rm` is a sequence of cache requests

### Run Command

To run the program, use the following command:

```
python <PATH TO main.py> --input <PATH TO INPUT FILE> [--output <PATH TO OUTPUT FILE>]
```

If an output file path is not provided, the output will be printed to standard out.

Examples:

```
python src/main.py --input tests/example.in
```

```
python src/main.py --input tests/example.in --output tests/example.out
```

### Output Format

The program outputs the results of the cache eviction policies in the following format:

```
FIFO  : <NUMBER OF MISSES>
LRU   : <NUMBER OF MISSES>
OPTFF : <NUMBER OF MISSES>
```

The output will be written to either an output file or the terminal, depending on how the program was run.

# Written Component

## Question 1

| Input | k   | m   | FIFO | LRU | OPTFF |
| ----- | --- | --- | ---- | --- | ----- |
| file1 |     |     |      |     |       |
| file2 |     |     |      |     |       |
| file3 |     |     |      |     |       |

## Question 2

## Question 3
