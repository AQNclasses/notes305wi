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


# Problem 2

Prove that every integer greater than 1 has a prime divisor.

Hint: two cases to consider for a given integer *n*. Use strong induction.

# Problem 3

Prove that all trees with $n$ vertices contain $n-1$ edges.


# Problem 4

Any convex polygon $P$ with $k \geq 3$ vertices can be decomposed into a set of
$k-2$ triangles whose interiors do not overlap.
