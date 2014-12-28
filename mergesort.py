'''
38-----27-----43-----3-----9-----82-----10
38-----27-----43-----3     9-----82-----10
38-----27     43-----3     9-----82     10
38     27     43     3     9     82     10
27-----38     3-----43     9-----82     10
3------27-----38----43     9-----10-----82
3-------9-----10----27----38-----43-----82

merge sort breaks up into subarrays... this allows the heavy lifting to be a
linear merge of sorted subarrays at each step

two main functions:
merge_sort(m):
  split input array m into left and right parts and recursively calls itself
  with the subarrays.
    return merged left and right arrays after sorting
    return m if len(m) == 1
merge(left, right):
  perform a linear merge of left and right arrays, which are already sorted
  in order of smallest to largest

'''

def merge_sort(m):
  if len(m) == 1:
    return m
  else:
    middle = len(m) // 2
    # left = merge_sort(m[:middle])
    right = merge_sort(m[middle:])
    m = merge_sort(m[:middle])
    return merge(m, right)

# SLOWER: linear merge from smallest to largest, with pop(0)
# def merge(left, right):
#   result = []
#   while len(left) > 0 and len(right) > 0:
#     if left[0] <= right[0]:
#       result.append(left.pop(0))
#     else:
#       result.append(right.pop(0))
#   result += left
#   result += right
#   return result

# FASTER: linear merge from largest to smallest, with pop(-1)
def merge(left, right):
  # pop() is constant time, whereas pop(0) is not; do linear merge backwards
  result = []
  while len(left) > 0 and len(right) > 0:
    if left[-1] >= right[-1]:
      result.append(left.pop())
    else:
      result.append(right.pop())
  result += list(reversed(left))
  result += list(reversed(right))
  return list(reversed(result))

def sort(input_data):
  return merge_sort(input_data)
