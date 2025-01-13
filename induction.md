---
geometry:
  margin=1in
...


# Induction

1. Define your logical predicate P(n).
2. Prove that P(0) is true.
3. Prove that P(n) implies P(n+1).
   - often done by proving P(n) assuming all P(1), P(2), ..., P(n-1) are true
   - these are termed weak and strong induction, respectively


# Problem 1

Prove that for all n in the nonnegative integers,

$$
1 + 2 + ... + n = \frac{n(n+1)}{2}
$$

## Solution

For the base case, our $P(0)$ is really $P(1)$. The above formula is somewhat ill-defined, but let's assume it represents the sum from 1 to n. In that case, $P(n=1)$ can be proved trivially:

$$
1 = \frac{1(1+1)}{2} \\
1 = 1
$$

For the case of $P(n)$, we assume $P(n)$ to be true (inductive hypothesis), and directly compute $P(n+1) = P(n) + (n+1)$ as

$$
\startmathalignment[number=auto]
P(n+1) \NC = \frac{n(n+1)}{2} + (n+1) \NR
\NC = \frac{n^2 + n + 2n +2}{2} \NR
\NC = \frac{(n+1)(n+2)}{2}
\stopmathalignment
$$

yielding the expression to be proved for $P(n+1)$, and completing the proof by induction.

# Problem 2

Prove that every integer greater than 1 has a prime divisor.

Hint: two cases to consider for a given integer *n*. Use strong induction.

## Solution

Case 1: $n$ is prime, and divides itself.

Case 2: $n$ is not prime, so it must be a compound of two non-prime integers. Crucially, these integers are also *smaller* than $n$.

If we let $n = a \dot b$, with $a, b < n$, then by our inductive hypothesis, both $a$ and $b$ have prime divisors.

Then let $a/d$ be an integer, with $d$ any prime divisor of $a$.

The quantity $(n/a)(a/d)$ is the product of two integers, and thus the simplification $n/d$ must also be an integer.

Thus proving that $n$ has a prime divisor.

# Problem 3

Prove that all trees with $n$ vertices contain $n-1$ edges.

## Solution

Base case: The smallest tree has $n=1$ vertex, and $n-1 = 0$ edges.

Consider an arbitrary tree with $n$ vertices.

Remove an arbitrary edge from the tree. The result will be two disjoint trees (proof by contradiction: otherwise, the original tree would contain a cycle), let these be called tree $S$ with $k \in [1..n]$ vertices, and tree $T$ with $n-k$ vertices.

By our inductive hypothesis, tree $S$ contains $k-1$ edges and tree $T$ contains $(n-k)-1$ edges.

Consider merging these trees by adding an edge between any two vertices $s \in S$ and $t \in T$. The result must be a tree, no cycle can be created since there was no path from $s$ to $t$ betwen two disjoint trees.

The resulting tree will contain $(k-1) + (n-k-1) + 1 = n-1$ edges, thus proving the result by induction.


# Problem 4

Any convex polygon $P$ with $n \geq 3$ vertices can be decomposed into a set of
$n-2$ triangles whose interiors do not overlap.

## Solution

Base case: smallest polygon has $n=3$ vertices, equivalent to a single triangle.

Next, consider an arbitrary convex polygon with $n$ vertices.

By definition of convexity, we can add an edge between any two nonadjacent vertices in $P$. This edge is guaranteed not to overlap any edges of the polygon.

This added edge decomposes $P$ into two smaller nonoverlapping polygons, $Q$ and $R$. $Q$ has $k \in [3..(n-3)]$ vertices, and $R$ has $n-k+2$ vertices (the +2 from the two vertices the polygons share).

Thus, by our inductive hypothesis, $Q$ can be decomposed into $(k-3)$ triangles and $R$ can be decomposed into $(n-k)$ triangles.

The sum of the number of triangles in these two smaller polygons is $n-3$ triangles to compose our original polygon $P$, thus proving the statement by induction.
