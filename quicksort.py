# quicksort(A, lo, hi):
#   if lo < hi:
#     p := partition(A, lo, hi)
#     quicksort(A, lo, p - 1)
#     quicksort(A, p + 1, hi)

A = [3,7,8,5,2,1,9,5,4]

def quicksort(A):
    if len(A) <= 1:
        return A
    else:
        p = A[len(A)-1]
        sort = A[0:len(A)-1]
        less = []
        more = []
        for i in sort:
            if i > p:
                more.append(i)
            else:
                less.append(i)
        less = quicksort(less)
        more = quicksort(more)
        return less + [p] + more

print quicksort(A)
