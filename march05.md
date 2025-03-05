# Heap Sort

## Heaps

- A (binary) heap can be considered a nearly complete binary tree.
- Tree is filled on all levels except possibly the last, which must be filled
from left to right.
- Can be stored in arrays

## Max- and min-heaps

A max-heap $A$ must satisfy the condition

$$
A\[parent(i)\] \geq A[i]
$$

such that children cannot hold data values greater than their parents.

A min-heap is organized in the opposite way, so that children will be greater
than or equal to their parents.

Heaps often used to implement priority queues.

**Height** of node on heap is the number of *edges* on the longest downward path
from the node to a leaf.

```
Max-Heapify(A, i):
  l = left(i)
  r = right(i)
  if l <= A.heap_size and A[l] > A[i]:
    largest = l
  else:
    largest = i
  if r <= A.heap_size and A[r] > A[largest]:
    largest = r
  if largest != i:
    swap A[i] and A[largest]
    Max-Heapify(A, largest)
```

How to analyze?

For tree rooted at node $i$, we have $\Theta(1)$ operations to fix $A[i]$
$A[left(i)]$ and $A[right(i)]$, plus one recursive call on one of the children.

Child subtrees have size at most $2n/3$. Why?

Nodes in left subtree:

$$
1 + 2+ 4 + i + \ldots + 2^{h+1} = 2^{h+2} -1
$$
