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

| Input | k  | m   | FIFO | LRU | OPTFF |
| ----- |----| --- | ---- | --- | ----- |
| test0 | 3  | 50  | 42   | 42  | 31    |
| test1 | 5  | 100 | 74   | 68  | 29    |
| test2 | 10 | 200 | 149  | 142 | 78    |


#### Does OPTFF have the fewest misses?
OPTFF always has the fewest misses by a significant margin.

#### How does FIFO compare to LRU?
FIFO and LRU are very comparable and typically have very close numbers. 
In test0 and test2 I used completely randomly generated numbers, in which case LRU and FIFO give very similar numbers.
In test1 I inserted the number 10 more frequently to simulate the same data being accessed over and over. 
In scenarios with data frequently reaccessed not in succession LRU tends to perform better but with completely random requests they work in about the same time.


## Question 2

## Question 3
