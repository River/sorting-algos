import sys
import random

def gen_rand_file(filename, output_size):
  with open(filename, 'w') as f:
    for i in range(output_size):
      f.write('%i\n' % random.randrange(1000))

def is_number(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def main():
  # omit the [0] element, which is the script itself
  args = sys.argv[1:]

  # make sure there are at least two args and that the first one is an int
  if len(args) < 2 or not is_number(args[0]):
    print('usage: output-size output-file [output-file ...]')
    sys.exit(1)

  output_size = int(args[0])
  del args[0]

  for file in args:
    gen_rand_file(file, output_size)
    print('Wrote to %s' % file)

if __name__ == '__main__':
  main()
