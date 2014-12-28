'''
Selection sort. simple but O(n^2) complexity
'''

def sort(data):
  sorted_data = []
  for i in range(len(data)):
    i_min = 0
    for i in range(1,len(data)):
      if data[i] < data[i_min]:
        i_min = i
    sorted_data.append(data[i_min])
    del data[i_min]
  return sorted_data
