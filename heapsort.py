def build_heap(data):
  # build heap iteratively by adding each node and max heapifying after each
  # step; n iterations of log(n) complexity, therefore this process is O(nlogn)
  heap = [data[0]]
  for d in data[1:]:
    # insert new point as leftmost leaf at highest level
    heap.append(d)
    # max-heapify, by swapping with parent until parent is larger
    heap = max_heapify_up(heap, len(heap)-1)
  return heap

def max_heapify_up(heap, i):
  # if this is the root node, then we are done
  if i == 0:
    return heap
  else:
    # if parent is smaller, then swap with parent
    p = (i - 1) // 2
    if heap[p] < heap[i]:
      heap[p], heap[i] = heap[i], heap[p]
      return max_heapify_up(heap, p)
    # if parent is not smaller, then we are done
    else:
      return heap

def max_heapify_down(heap, i):
  # this node has two children
  if 2*i+2 <= len(heap)-1:
    # if left child is larger than node, and >= to right child,
    # swap left child and node
    if heap[2*i+1] > heap[i] and heap[2*i+1] >= heap[2*i+2]:
      heap[2*i+1], heap[i] = heap[i], heap[2*i+1]
      return max_heapify_down(heap, 2*i+1)
    # if right child is larger than node, and >= to left child
    # swap right child and node
    elif heap[2*i+2] > heap[i] and heap[2*i+2] >= heap[2*i+1]:
      heap[2*i+2], heap[i] = heap[i], heap[2*i+2]
      return max_heapify_down(heap, 2*i+2)
    # if both children are smaller, than we are done
    else:
      return heap
  # this node has only one child
  elif 2*i+1 <= len(heap)-1:
    # if child is larger, swap it with node
    if heap[2*i+1] > heap[i]:
      heap[2*i+1], heap[i] = heap[i], heap[2*i+1]
      return max_heapify_down(heap, 2*i+1)
    # if child is not larger, than we are done
    else:
      return heap
  # if this node has no more children, then we are done
  else:
    return heap

def heap_sort(data):
  heap = build_heap(data)
  sorted_data = []
  while len(heap) > 1:
    # take root node of the heap (largest value)
    # move rightmost child to the root
    sorted_data.append(heap[0])
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    del heap[len(heap)-1]
    # heap is now broken; fix heap by traversing downwards
    heap = max_heapify_down(heap, 0)
  sorted_data += heap
  return list(reversed(sorted_data))

def sort(data):
  return heap_sort(data)
