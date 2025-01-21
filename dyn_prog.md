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
RecFibo(n):
  if n=0:
    return 0
  elif n=1:
    return 1
  else
    return RecFibo(n-1) + RecFibo(n-2)
```

Let $T(n)$ be the number of calls to `RecFibo`. Then, we have the recurrence

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
- So our recursive algorithm takes about twice as long as a procedural solution :(
- Even worse, growth is exponential in $n$.
- How to show?

Modify original recurrence to inequality:

1. $F_n = F_{n-1} + F_{n-2}$
2. $F_{n-1} = F_{n-2} + F_{n-3}$

Substituting 2. into 1.:

$$
F_n = 2F_{n-2} + F_{n-3}
$$

Dropping the $F_{n-3}$ term, and creating an inequality:

$$
F_n > 2F_{n-2}
$$

## Sidebar: Solving Recurrence Relations with roots of characteristic equation

- Method for generating solutions to recurrence relations of form $f_n + \alpha f_{n-1} + \beta f_{n-2} = 0$
- We guess that $f_n = r^n$, then factor and solve for $r$
- Example:

$$
G_n = G_{n-1} + 6 G_{n-2} \\
\to r^n - r^{n-1} - 6r^{n-2} = 0 \\
\to r^{n-2} ( r^2 - r - 6 ) = r^{n-2} (r-3) (r+2)
$$
