'''
Runs sorting algorithms with input data, checks that values are sorted, and
returns running times of the scripts.
'''

import sys
import time

def is_sorted(data):
  return all(data[i] <= data[i+1] for i in range(len(data)-1))

def main():
  args = sys.argv[1:]

  if len(args) < 2:
    print('usage: [--output] input-file sorting-algorithm [sorting-algorithm ...]')
    sys.exit(1)

  print_output = False
  if args[0] == '--output':
    print_output = True
    del args[0]

  input_file = args[0]
  del args[0]
  try:
    with open(input_file) as f:
      input_data = [int(i) for i in f.readlines()]
  except FileNotFoundError:
    print('Unable to import data')
    sys.exit(1)
  except ValueError:
    print('Input data must consist of int values')
    sys.exit(1)

  for sorting_algo in args:
    if sorting_algo[-3:] == '.py':
      sorting_algo = sorting_algo[:-3]

    try:
      algo = __import__(sorting_algo)
      start = time.time()
      output_data = algo.sort(input_data)
      end = time.time()
    except (ImportError, NameError):
      print('Unable to import sorting algorithm')
      sys.exit(1)

    print('%s.py: %.4fs to sort %i numbers' %
      (sorting_algo, end-start, len(input_data)))
    print(' - Input data sorted...  %s' % ((' NO','YES')[is_sorted(input_data)]))
    print(' - Output data sorted... %s' % ((' NO','YES')[is_sorted(output_data)]))
    if print_output:
      print(output_data)
    print('')

if __name__ == '__main__':
  main()
