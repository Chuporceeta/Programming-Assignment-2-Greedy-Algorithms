import os
import argparse

def FIFO(k, requests):
    misses = 0
    cache = []
    hit = False
    for i in range(len(requests)):
        hit = False
        for j in range(len(cache)):
            if cache[j] == requests[i]:
                hit = True
                break
        if not hit:
            misses += 1
            cache.append(requests[i])
            if len(cache) > k:
                cache.pop(0)

    return misses

def LRU(k, requests):
    # k = cache size

    return 0

def OPTFF(k, requests):
    num_misses = 0
    cache = set()

    for i, request in enumerate(requests):
        if request not in cache:
            num_misses += 1
            if len(cache) == k:
                eviction_candidates = cache.copy()
                for req in requests[i+1:]:
                    if len(eviction_candidates) == 1:
                        break
                    if req in eviction_candidates:
                        eviction_candidates.remove(req)
                for victim in eviction_candidates:
                    cache.remove(victim)
                    break
            cache.add(request)

    return num_misses

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=False)
    args = parser.parse_args()

    input_file = args.input
    assert os.path.exists(input_file), "Input file does not exist"
    output_file = args.output

    with open(input_file) as f:
        # validate file is not empty
        assert os.stat(input_file).st_size != 0, "Error: input file is empty"

        k, m = [int(x) for x in f.readline().split()]
        requests = [int(x) for x in f.readline().split()]

        assert k >= 1, "Error: cache size must be at least 1"

    print("FIFO:", FIFO(k, requests))
    print("LRU:", LRU(k, requests))
    print("OPTFF:", OPTFF(k, requests))