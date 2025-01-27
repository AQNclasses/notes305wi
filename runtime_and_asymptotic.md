# Computing runtime

- So far, we've been looking a lot at recurrences and how to analyze recursive
algorithms.
- Quick refresh of "non-recursive" runtime analysis
- Counting!

```python
def example(n):
    j = 0                   # 1 assignment
    j += 1                  # 1 operation
    for i in range(1,n):    # 1 assignment to initialize, one for each increment = n+1
      j = 1                 # n (cost one, inside for loop)
      while j <= n:         # one evaluation per iteration of inner loop
         j += 2             # 1 operation per iteration of inner loop
```

- How many times will inner loop evaluate for arbitrary `i`?
- Can estimate `n/2` by inspection
- Algebra solution:
  - after $k$ iterations, value of `j` is `2k+1`
  - Termination condition: `j <= n`
  - Solve for value of k when loop terminates: `2k+1 <= n` -> `k = (n-1)/2`
- So inner loop will run $(n-1)/2$ times during *each* iteration of outer loop
- Total count -> $n*c*(n-1)/2$
- What if inner loop instead terminates when $j <= i$??
  - Can simply multiply max runtime by $n$ (over-estimation)
  - To get tighter bound, manually compute sum over i

$$
\sum_{i=1}^n (i-1)/2
$$

$$
\to \frac{1}{2} \sum_{i=1}^n (i-1)
$$

$$
\to \frac{1}{2} \big((\sum_{i=1}^n i) - n \big)
$$

# Tips and Tricks

- Arithmetic series finite sum
  - Example: $1 + 2 + \ldots + n$
  - Example: $2 + 5 + 8 + 11 + 14 = 40$
  - Formula: $\frac{n(a_1 + a_n)}{2}$
- Geometric series sum
  - $\sum_{i=0}^n a r^i$
  - Case of $r=1$
  - Otherwise, sum = $a\frac{1-r^{n+1}}{1-r}$
- Logarithm rules (+ exponent rules)
- Don't stress about floor / ceilings
- Big theta: mostly we care about showing that lower and upper bound have same
  functional form. To justify, need to justify that there is no situation where we
  will change the functional form of the runtime expression $T(n)$.

# Example 1

Consider a straightforward implementation of insertion sort.

```python
def insertionSort(arr):
  for i in range(1, len(arr)):          # n+1
    key = arr[i]                        # n
    j = i-1                             # n

    while j >= 0 and key < arr[j]:      # best case: 2; worst case: n
      arr[j+1] = arr[j]                 # 1*above
      j -= 1                            # 1*above
    arr[j+1] = key                      # n
```

# Notation

## O-notation

O-notation characterizes an upper bound on the asymptotic behavior of a function.

O-notation implies that a function grows *no faster* than a certain rate. The rate is determined by
the highest order term.

For example, $f(n) = 7n^3 + 100n^2 - 20n + 6$ is $O(n^3)$.

The function $f(n)$ is also $O(n^5)$, and in general is $O(n^c) for any constant $c \geq 3$.

## Ω-notation

Ω-notation characterizes a lower bound on the asymptotic behavior of a function, implying that a function grows
*at least as fast* as a certain rate. Again, this rate is based on the highest-order term.

Using the same function $f(n) = 7n^3 + 100n^2 - 20n + 6$, $f(n)$ is $\Omega(n^3)$.

The function $f(n)$ is also $\Omega(n^2)$, $\Omega(n)$, and $\Omega(n^c)$ for any $c \leq 3$.

## Θ-notation

$\Theta$-notation characterizes a *tight bound* on the asymptotic behavior of the function: it states
that a function grows at precisely a certain rate, based on the highest-order term (in the limit of large $n$).

Our example function $f(n) = 7n^3 + 100n^2 - 20n + 6$ is $\Theta(n^3)$, and is $\Theta(n^c}$ only for $c=3$.

The logical relationship between the notations is:

$$
O(f(n)) \wedge \Omega(f(n)) \iff \Theta(f(n))
$$
