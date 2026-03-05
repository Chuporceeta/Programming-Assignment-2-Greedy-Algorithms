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
| ----- |----| --- |------|-----| ----- |
| test0 | 3  | 50  | 42   | 42  | 31    |
| test1 | 5  | 100 | 49   | 48  | 29    |
| test2 | 10 | 200 | 149  | 145 | 78    |


#### Does OPTFF have the fewest misses?
OPTFF always has the fewest misses by a significant margin.

#### How does FIFO compare to LRU?
FIFO and LRU are very comparable and typically have very close numbers. 
In test0 and test2 I used completely randomly generated numbers, in which case LRU and FIFO give very similar numbers.
In test1 I inserted the number 10 more frequently to simulate the same data being accessed over and over. 
In scenarios with data frequently reaccessed (not in succession) LRU tends to perform better but with completely random requests they work in about the same time.

## Question 2
#### For ( k = 3 ), investigate whether there exists a request sequence for which OPTFF incurs strictly fewer misses than FIFO.

1 2 3 4 2 1
FIFO misses: 5
OPTFF misses: 4

#### In either case, briefly explain your reasoning.
There does exist a sequence where OPTFF has fewer misses than FIFO for (k=3).
OPTFF ejects the item in the cache that is accessed again the farthest in the future. It minimizes cache misses by ensuring the only elements ejected from the cache are not used until much later.
FIFO on the other hand only holds recently accessed data. So though it is good for accessing data over and over again, it does not have the foresight that OPTFF has that makes OPTFF so efficient in most scenarios.

## Question 3

Let $A$ be any offline algorithm that knows the full request sequence.

Let $R=\{r_1, r_2, ... r_m\}$ be a sequence of cache requests.

Let $S_A$ be the eviction schedule produced from running $A$ on $R$, and let $S_{FF}$ be the eviction schedule produced from running Belady’s Farthest-in-Future algorithm on $R$.

Since Belady's algorithm does not bring items into the cache unless there is a cache miss, $S_{FF}$ is a reduced schedule. We can transform $S_A$ into a reduced schedule $\bar S_A$ that brings in at most the same amount of items as $S_A$: whenever $S_A$ brings in an item $d$ on step $i$ that was not requested, $\bar S_A$ does nothing on step $i$ and only brings $d$ in on a later step $j$ when it is requested. The cost of bringing in $d$ on step $i$ is then just moved to step $j$, or eliminated outright if $d$ is never requested.

Let $j$ be any integer such that $\bar S_A$ and $S_{FF}$ agree on the first $j$ requests. Thus the state of the cache is the same for both algorithms when processing request $r_{j+1}$.

We will construct a schedule $S'$ that agrees with $S_{FF}$ on the first $j+1$ requests without bringing in more items than $\bar S_A$ overall.

Case 1: $r_{j+1}$ is in the cache. Then neither schedule evicts (because they are reduced), so let $S'$ = $\bar S_A$.

Case 2: $r_{j+1}$ is not in the cache.

- Case 2a: $\bar S_A$ and $S_{FF}$ evict the same item. Then let $S'$ = $\bar S_A$.
- Case 2b: $\bar S_A$ evicts some item $a$ while $S_{FF}$ evicts some item $b$, $a \neq b$. Then let $S'$ agree with $S_{FF}$ for the first $j+1$ requests. For the remaining requests, let $S'$ agree with $\bar S_A$ unless:
  - $c \neq b$ is requested and $\bar S_A$ would evict $b$: Then $S'$ evicts $a$.
  - $a$ is requested and $\bar S_A$ would evict $c$: If $c \neq b$, then $S'$ evicts $c$ and brings in $b$.

  In either case, $S'$ brings in as many items as $S_A$ and ends up with the same cache afterwards. We know that $b$ will never be requested before $a$ because $b$ was selected by $S_{FF}$.

By induction on $j$, $S'$=$S_{FF}$ and $S'$ does not bring in more items than $\bar S_A$. Therefore, $S_{FF}$ does not bring in more items than $S_A$, so Belady's Farthest-in-Future algorithm cache misses no more times than $A$.
