# quicksort(A, lo, hi):
#   if lo < hi:
#     p := partition(A, lo, hi)
#     quicksort(A, lo, p - 1)
#     quicksort(A, p + 1, hi)

def quicksort(A):
    if len(A) <= 1:
        return A
    else:
        p = A[0]

        less = []
        pivot = []
        more = []

        for i in A:
            if i > p:
                more.append(i)
            elif i < p:
                less.append(i)
            else:
                pivot.append(i)

        less = quicksort(less)
        more = quicksort(more)
        return less + pivot + more

def sort(data):
  return quicksort(data)
