#! /usr/bin/python

import random

def partition(A, p, r):
    x = A[random.randint(p,r)]

    print(f"Pivot is {x}")
    i = p-1
    swap = 0
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            swap = A[i]
            A[i] = A[j]
            A[j] = swap
    swap = A[i+1]
    A[i+1] = A[r]
    A[r] = swap
    return i+1

def quicksort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

A = [10,9,8,7,6,4,2,1,5]
print(A)
quicksort(A, 0, len(A)-1)
print(A)
