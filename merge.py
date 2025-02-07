import matplotlib.pyplot as plt
import numpy as np
import time

test = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

test2 = np.array([6, 7, 8, 9, 10, 1, 2, 3, 4, 5])

def mergeSort(A, k):
    n = A.size
    if n > k:
        m = n // k
        for i in range(k):
            start = i*m
            stop = (i+1)*m
            if n - stop < m:
                stop = n
            #print(f"Start: {start}, Stop: {stop}, n: {n}")
            #print(f"New Array {A[start:stop]}")
            mergeSort(A[start:stop], k)
        for i in range(k):
            merge(A, m*i)
        #print(A)

def merge(A, m):
  B = np.zeros(A.size, dtype=A.dtype)
  i = 0
  j = m

  for k in range(A.size):
      if j >= A.size:
          B[k] = A[i]
          i += 1
      elif i >= m:
          B[k] = A[j]
          j += 1
      elif A[i] <= A[j]:
          B[k] = A[i]
          i += 1
      else:
          B[k] = A[j]
          j += 1

  for k in range(A.size):
      A[k] = B[k]


if __name__ == '__main__':
    mergeSort(test, 3)
    print(test)
