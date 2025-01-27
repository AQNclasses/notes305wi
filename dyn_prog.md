---
title: Dynamic Programming Lecture Notes
author: Alexandra Nilles
date: Winter 2025
---

# 21 January 2025

## Admin

- HW 1 due tonight 10pm
  - Upload on Canvas
  - If handwritten, use scanning app or scanner in library, computer labs
  - Submission is PDF only
- Quiz Friday
  - Credit for attempts
  - 30 minutes given, aim for 15 mins
  - handwritten / handtyped solutions

## Making the Best of It: Efficient Backtracking?

- (Show schedule)
- Recall we started with counting and recurrences to find our resource usage function $T(n)$
  - Counting for imperative code
  - Recurrences for recursive code
- Example: Fibonnaci numbers

<!--
# conTeXt for accessible PDF - TODO check if this is necessary now that compiling with context seems to be working for regular math mode
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
- How to show?


## Sidebar: Solving Recurrence Relations with roots of characteristic equation

- Method for generating solutions to recurrence relations of form $f_n + \alpha f_{n-1} + \beta f_{n-2} = 0$
- We guess that $f_n = r^n$, then factor and solve for $r$
- Example:

$$
\begin{align*}
& G_n = G_{n-1} + 6 G_{n-2} \\
\to & r^n - r^{n-1} - 6r^{n-2} = 0 \\
\to & r^{n-2} ( r^2 - r - 6 ) = r^{n-2} (r-3) (r+2)
\end{align*}
$$

Solutions $r=3$ and $r=-2$ are both valid, depending on initial conditions (check using original recurrence).

Solutions of $f_n + \alpha f_{n-1} + \beta f_{n-2} = 0$ can be found using roots
$r_1$, $r_2$ of the characteristic equation $x^2 + \alpha x + \beta = 0$, and in general solutions
take the form $f_n = a r_1^n + b r_2^n$.

Further reading [here](https://discrete.openmathbooks.org/dmoi2/sec_recurrence.html) and [here](https://math.stackexchange.com/a/167197).

`https://discrete.openmathbooks.org` is a great resource in general.

## Back to Fibonacci

$$
F_n = F_{n-1} + F_{n-2}
$$

implies the characteristic equation $x^2 - x - 1 = 0$, with roots

$$
r = \frac{1 \pm \sqrt{5}}{2}
$$

The positive root gives the solution $F_n \approx 1.618^n$ (golden ratio!).

## Memo-ization

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

\newpage

# 27 January 2025

## Amortization Recap

Stack implementation, doubling in size every time we resize, has a total resize cost of

$$
\sum_{i=0}^k 2^i
$$

such that for an input of size $n$, the final (kth) resize has the property $2^k <= n$. Thus our upper bound is
$k <= lg n$, and we take the upper bound $k = lg n$ for our runtime analysis.

In the more general case of summation to $N$, this is a geometric series, so we can apply our general formula

$$
\sum_{i=0}^N r^i = \frac{1-r^{N+1}}{1-r}
$$

to find

$$
\sum_{i=0}^{lg n} 2^i = 2^{1 + lg n}-1 = 2 \dot 2^{lg n} - 1 = 2 n - 1.
$$

The result can also be shown inductively.

## Text Segmentation

Recall the text segmentation problem where we are given a string $A[1..n]$ and a constant-time boolean subroutine `isWord`.

We wish to decide whether the input $A$ can be partitioned into a sequence of words.
