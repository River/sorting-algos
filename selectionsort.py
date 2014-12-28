'''
Selection sort. simple but O(n^2) complexity
'''

def sort(data):
  sorted_data = []
  unsorted_data = list(data)
  for i in range(len(unsorted_data)):
    i_min = 0
    for i in range(1,len(unsorted_data)):
      if unsorted_data[i] < unsorted_data[i_min]:
        i_min = i
    sorted_data.append(unsorted_data[i_min])
    del unsorted_data[i_min]
  return sorted_data
