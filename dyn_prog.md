---
title: Dynamic Programming Lecture Notes
author: Alexandra Nilles
date: Winter 2025
---


# Making the Best of It: Efficient Backtracking with Dynamic Programming

## Example 1

Consider the Fibonnaci numbers.

<!--
# conTeXt for accessible PDF
\startformula
F_n =
 \startmathcases
  \NC 0 \NC n = 0 \NR
  \NC 1 \NC n = 1 \NR
  \NC F_{n-1} + F_{n-2} \NC otherwise \NR
 \stopmathcases
\stopformula
-->

$$
F_n = \begin{cases}
0 & n = 0 \\
1 & n = 1 \\
F_{n-1} + F_{n-2} & otherwise
\end{cases}
$$

Giving us the sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...

In pseudocode (assuming n > 0):

```python
RecFib(n):
  if n=0:
    return 0
  elif n=1:
    return 1
  else
    return RecFib(n-1) + RecFib(n-2)
```

Let $T(n)$ be the number of calls to `RecFib`. Then, we have the recurrence

$$
\begin{align*}
T(0) & = 1, \\
T(1) & = 1, \\
T(n) & = T(n-1) + T(n-2) + 1,
\end{align*}
$$

- Write out values of T(n): 1, 1, 3, 5, 9, ...
- Progressing like the fibonacci numbers. Guess general form $T(n) = A \dot F_{n+1} + B$
- Solve to find $T(n) = 2 F_{n+1} - 1$
- So our recursive algorithm takes about twice as many operations as counting by ones to $F_{n+1}$ :(
- Even worse, resource function $T(n)$ growth is exponential in $n$.
- How to show? See [here](runtime_and_asymptotic.md#root-method).

Considering our original recurrence

$$
F_n = F_{n-1} + F_{n-2}
$$

implies the characteristic equation $x^2 - x - 1 = 0$, with roots

$$
r = \frac{1 \pm \sqrt{5}}{2}.
$$

The positive root gives the solution $F_n \approx 1.618^n$ (golden ratio!).
Since this value is larger than one, a naive recursive algorithm would run in
time exponential in $n$.

### Memo-ization

Define a hash map `F` with entries `F[n]`.

```python
F = {}
MemFib(n):
  if n==0 or n==1:
    return n
  else:
    if n not in F:
      F[n] = MemFib(n-1) + MemFib(n-2)
    return F[n]
```

How many additions? Let's try it!

Now that we have very cleverly figured out how to compute Fibonacci numbers in linear time, we
can write an algorithm to explicitly fill up a memo-ization array in order, instead of computing
with our cached values recursively on the stack.

```python
import numpy as np

IterFib(n):
  f = np.zeros(n+1)
  F[0] = 0
  F[1] = 1
  for i in range(2, n+1):
      F[n] = F[n-1] + F[n-2]
    return F[n]
```

We can also refine this further to save space, by only tracking two integers:

```python
IterFib2(n):
  prev = 1
  curr = 0
  for i in range(1, n+1):
    next = curr + prev
    prev = curr
    curr = next
  return curr
```

While in this case, even if we could have written the maximally efficient approach from the start,
this is a much more general technique for optimizing recursive algorithms. Often, especially when
working with specialized data structures (graphs, heaps, etc.) it is easier to define an algorithm
recursively first.

## Example 2


Recall the text segmentation problem where we are given a string $A[1..n]$ and a constant-time boolean subroutine `isWord`.

We wish to decide whether the input $A$ can be partitioned into a sequence of words.

We defined a function `Splittable(i)` that returns True if and only if the suffix $A[i..n]$ can be partitioned into a sequence of words.

Then, we can solve the problem by computing `Splittable(1)`.

We can write down the recurrence as

$$
Splittable(i) = \begin{cases}
True & \text{if $i > n$} \\
\vee_{j=1}^n isWord(i,j) \wedge Splittable(j+1) & \text{otherwise}
\end{cases}
$$

but this recurrence, translated directly into a recursive function, runs in $O(2^n)$ time in the worst case.

Is this reasonable?

- How many ways to call `Splittable`?
- How many ways to call `isWord`?

What does this imply about how we should memoize the algorithm?

- We want to build up solutions from the end of the input array to the beginning, because computing `Splittable(i)`
- depends on results for `Splittable(j)` for all valid $j > i$.


## Example 3

Problem: Independent Set

Definition of independent set of a graph: subset of vertices with no edges
between them.

Finding maximum size independent set is a canonical NP-hard problem.

But when the input graph is a tree with $n$ vertices, we can compute the largest independent set
in $O(n)$ time.

Assume we are given a tree T, with a root.

For any node v in T, let MIS(v) denote the size of the largest independent set
in the subtree rooted at v.

There are two cases for the independent set of this tree: includes $v$ or
doesn't.

If the independent set includes $v$, it cannot include any of $v$'s direct
children, but will include the independent sets of $v$'s "grandchildren."
If the independent set does not include $v$, then the independent set
can be written as the union of the independent sets of the subtrees rooted at
children of $v$.

(draw on board)

Let $c(w)$ be a function that returns the children of vertex $w$. Then, our
observation above implies the following recurrence:

$$
MIS(v) = \text{max} \left. \begin{cases}
\sum\limits_{w \in c(v)} MIS(w) & \text{excluding v} \\
1 + \sum\limits_{w \in c(v)} \sum\limits_{x \in c(w)} MIS(x) & \text{including v}
\end{cases} \right\\}
$$


What kind of data structure should we use to memoize this recurrence? (Tree!)

How? (can add binary variable to nodes, to keep or to skip, as well as storing
MIS(x) for each x when it is computed)

In what order must we visit the nodes? Every vertex must be visited before its
parent, requiring a post-order traversal.

### Runtime Analysis

Hard to determine runtime from recurrence: sums will be different sizes at
different levels, and dependent on tree structure.

But consider: Each vertex contributes a constant amount of time to its parent
and grandparent's computations of MIS. Each vertex has at most one parent and at
most one grandparent. So, counting only the contributions *up* the tree from
each node, we conclude that this algorithm runs in $O(n)$ time.

### Algorithm

A full dynamic programming algorithm to find the size of the maximum
independent set can be written as:

```python
def TreeMIS(v):
  skip = 0
  for w in children(v):
    skip += TreeMIS(w)
  keep = 1
  for w in children(v):
    for x in children(w):
      keep += x.MIS # retrieve cached value
  v.MIS = max([keep, skip]) # cache value
  return v.MIS
```

Since we have defined this recursively in the correct order to give us a
postorder traversal, we will not repeat any computations.

## Example 4

Another fun problem from bioinformatics: edit distance!

The **edit distance** between two strings is the minimum number of letter
insertions, letter deletions, and letter substitutions required to transform one
string into the other.

For example, the edit distance between FOOD and MONEY is at most four:

```
FOOD
MOOD
MOND
MONED
MONEY
```

Intermediate states do not have to be valid words.

We can use a column representation to see why we must take at least four steps:

```
F O O   D
M O N E Y
```

We cannot get away with fewer than one insertion and three substitutions.

How to tell automatically what the shortest distance is?

Dynamic programming steps:

1. Identify recursive structure
2. Write down correct recurrence
3. Analyze recurrence to identify subproblems, dependencies, and memoize

### Recursive (Inductive) Structure

Take the gap representation for the minimal edit distance. If we remove the last
(or first - order is arbitrary) column, the remaining columns must represent the shortest edit
sequence for the remaining prefixes. Proof by induction: if the prefixes had a
shorter edit sequence, we could use that, glue the last column back on, and the
result would violate our original assumption of minimal edit distance.

So we are looking to find a sequence of editing operations. Editing operations
do not depend on previously chosen operations.

Another example:

```
AL TRUISTIC
ALGOR I THM
```

Thus, for any two input strings $A[1..m]$ and $B[1..n]$, we can create a
recursive function $Edit(i,j)$ that computes the edit distance between the
prefixes $A[1..i]$ and $B[1..j]$, and we need to compute $Edit[m,n]$.

### Recurrence

Three possibilities for each column:

- **Insertion:** In this case, we need one
insertion, and the edit distance is equal to $Edit(i, j-1) + 1$.

```
ALTR
ALGOR
```

- **Deletion:** In this case, the edit distance is equal to $Edit(i-1, j) + 1$.

```
ALTRU
ALGO
```

- **Substitution:** In this case, if we are comparing two different characters,
the edit distance is equal to $Edit(i-1, j-1) + 1$. If both characters are
equal, the "substitution" is free, so our edit distance is $Edit(i-1, j-1)$.

```
ALTRU
ALGOR
```

```
ALTRUI
ALGORI
```

- Special cases: if i=0 or j=0
- Transforming the empty string into a string of length $j$ requires $j$
insertions, so $Edit(0,j) = j$.
- Transforming a string of length $i$ into the empty string requires $i$
deletions, so $Edit(i,0) = i$.

So, we can write down our full recurrence as:

$$
Edit(i,j) = \begin{cases}
i & \text{if $j = 0$} \\
j & \text{if $i = 0$} \\
\text{min} \left. \begin{cases}
Edit(i,j-1) + 1 \\
Edit(i-1,j) + 1 \\
Edit(i-1, j-1) + [A[i] \neq B[j]]
\end{cases} \right\\} & \text{otherwise}
\end{cases}
$$

(explain indicator variable)

### Mechanical Memoization

- **Subproblems:** recursive subproblems are defined by $0 \leq i \leq m$ and
$0 \leq j \leq n$
- **Data structure:** We will have at most $m \cdot n$ values for $Edit(i,j)$,
so we can store in a two-dimensional array, $Edit[0 \ldots m, 0 \ldots n]$.
- **Dependencies:** Each entry $Edit(i,j)$ depends on three neighboring entries,
$Edit[i-1,j]$, $Edit[i, j-1]$, and $Edit[i-1, j-1]$.
- **Evaluation order:** If we use standard row-major order (left to right in
each row, from top row to bottom row), the entries will be defined in the
correct order.

How to initialize base cases?

### Performance Analysis

To fill out the table will take $O(mn)$ time and space. Computing each entry
takes constant time since we know its predecessors.

(Show memoization table)

Our table does not store arrows: how long does it take to reconstruct the
shortest edit sequence?

## Example 5

Our final example for dynamic programming / cacheing is the problem of forming
optimal binary search trees.

As input, we are given a sorted array $A[1..n]$ of search keys and an array
$f[1..n]$ of frequency counts, where $f[i]$ is the number of searches for
$A[i]$.

Our task is to construct a binary search tree for the set of keys such that the
total cost of all the searches is as small as possible.

How to find recurrence?

First, let's write down the total cost of all searches in an arbitrary tree $T$.
The cost of searching $A[i]$ will be the frequency $f[i]$ multiplied by the
depth of the node containing $A[i]$. So the total cost will be:

$$
Cost(T, f[1..n]) = \sum\limits_{i=1}^n f[i] * (depth(A[i] + 1)
$$

However, one of these nodes must be the root node. Let us set the root node at
i=r, which must have depth zero. Then, we can factor our sum as

$$
Cost(T, f[1..n]) = \sum\limits_{i=1}^n f[i] + \
\sum\limits_{i=1}^{r-1} f[i] * (depth_{left}(A[i] + 1) + \
\sum\limits_{i=r+1}^{n} f[i] * (depth_{right}(A[i] + 1)
$$

Where we have factored the sum into the contribution from the root, left and
right subtrees. The recursive structure is now more clear, and we can write:

$$
Cost(T, f[1..n]) = \sum\limits_{i=1}^n f[i] + \
Cost(T_{left}, f[1..r-1]) + \
Cost(T_{right}, f[r+1..n])
$$

So, it becomes clear that finding the optimal cost involves picking the correct
root at every level of execution. For this naive approach, our recurrence is
$T(n) = \alpha n + 2 \sum_{k=0}^{n-1} T(k)$. The solution is in your book, and
gives us $T(n) = O(3^n)$. How to improve?

First, let's write a recurrence for OptCost that explicitly searches over the
options for the root:

$$
OptCost(i,k) = \begin{cases}
0 & \text{if $i>k$} \\
\sum\limits_{j=i}^k f[j] + \min\limits_{i \leq r \leq k} \begin{cases}
OptCost(i, r-1) + OptCost(r+1,k) \end{cases} & otherwise
\end{cases}
$$

A lot going on here! First, let us separately memoize the sum in the first term.

Let $F(i,k)$ denote the total frequency count for all keys in interval
$A[i..k]$:

$$
F(i,k) = \begin{cases}
f[i] & \text{if $i=k$} \\
F(i, k-1) + f[k] & \text{otherwise}
\end{cases}
$$

Can compute all values in $O(n^2)$ time.

### Mechanical Memoization

Now we have:

$$
OptCost(i,k) = \begin{cases}
0 & \text{if $i>k$} \\
F[i,k] + \min\limits_{i \leq r \leq k} \begin{cases}
OptCost(i, r-1) + OptCost(r+1,k) \end{cases} & otherwise
\end{cases}
$$

- **Subproblems:** specified by $i$ and $k$. We require $i \leq k$.
- **Data Structure:** We can use a two dimensional array, and fill out half.
- **Dependencies:** Each entry depends on $OptCost[i, j-1]$ and
$OptCost[j+1,k]$ (left and below).

(draw evaluation order options on board)

- **Performance analysis:** Clearly require $O(n^2)$ space. However, each entry
requires evaluating up to $n$ different options for the minimum. Thus, we expect
$O(n^3)$ time.
