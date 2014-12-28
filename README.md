sorting-algos
=============

Practicing implementing sorting algorithms in python.

Use `generate-data.py` to generate files containing random integers from 1 to 1000 for benchmarking.

Use `benchmark.py` to run `*sort.py` modules, time the sorts, and check that the outputs are sorted.

`*sort.py` modules have a `sort(data)` method, which takes in an array and returns that array sorted.

Sample usage:
------------

```
$ python3 generate-data.py 1000 data/test
Wrote to data/test
$ python3 benchmark.py data/test *sort.py
heapsort.py: 0.0165s to sort 1000 numbers
- Input data sorted...   NO
- Output data sorted... YES

mergesort.py: 0.0113s to sort 1000 numbers
- Input data sorted...   NO
- Output data sorted... YES

quicksort.py: 0.0032s to sort 1000 numbers
- Input data sorted...   NO
- Output data sorted... YES

selectionsort.py: 0.0950s to sort 1000 numbers
- Input data sorted...   NO
- Output data sorted... YES

```
