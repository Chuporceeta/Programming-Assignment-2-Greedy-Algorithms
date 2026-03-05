import os
import argparse

def FIFO(k, requests):
    return 0

def LRU(k, requests):
    return 0

def OPTFF(k, requests):
    return 0

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