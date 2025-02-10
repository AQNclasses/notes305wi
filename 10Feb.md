# Announcements

- Quiz make-up policy: take on Canvas until the following Wednesday for partial
credit; email me if you need it re-opened.
- Resubmissions for HW1 due 2/13
- Grading HW2 without double penalties for things corrected in HW1
  - comment on your submission ASAP about who you worked with to avoid points lost
- Mid-term Friday: about 2x length of quizzes, will have entire class period
  - One 8.5"x11" single sided sheet of notes allowed (physical copy)
  - Paper preferred, computer OK
  - No other resources allowed (automatic zero and possibly fail the course).
  - Book in DAC reminder!
    - DAC exam will be taken on computer by default: remember to show your work!
    - No drawing of recursion trees is explicitly required, but may be one
      method you use to find a bound

# Last new content: Theorem for finding tight bounds

Imagine we have a recurrence of form:

$$
T(n) = a T(\frac{n}{b}) + f(n)
$$

with a base case $T(n) \in \Theta(1)$.

What are some examples?

- Merge sort: $T(n) = 2T(n/2) + n$
- Binary search: $T(n) = T(n/2)$
- Max sub-array: $T(n) = 2T(n/2) + \Theta(n)$

First, we define a *critical exponent* $c_{crit} = \log_b(a)$.

Three cases:

1. Work is dominated by subproblems.

   a. **Condition:** $f(n) = O(n^c)$ where $c < c_{crit}$.

   b. **Bound:** $T(n) = \Theta(n^{c_{crit}})$

2a.

   a. **Condition:** $f(n) = \Theta(n^{c_{crit}} \log^k(n)$ for $k > -1$.

   b. **Bound:** $T(n) = \Theta(n^{c_{crit}} \log^{k+1}(n))$

2b.

   a. **Condition:** $f(n) = \Theta(n^{c_{crit}} \log^k(n)$ for $k = -1$.

   b. **Bound:** $T(n) = \Theta(n^{c_{crit}} \log(\log(n)))$

2c.

   a. **Condition:** $f(n) = \Theta(n^{c_{crit}} \log^k(n)$ for $k < -1$.

   b. **Bound:** $T(n) = \Theta(n^{c_{crit}})$

3. Work to split/recombine dominates the subproblems.

   a. **Condition:** $f(n) = \Omega(n^{c_{crit}}$ where $c > c_{crit}$
   **and** $af(\frac{n}{b}) \leq k f(n)$ for $k < 1$ and sufficiently large $n$. Second
   condition is called the *regularity condition*.

   b. **Bound:** $T(n) = \Theta(f(n))$

Examples:

1. $T(n) = 8T(\frac{n}{2}) + 1000n^2$

Solution: Case 1

$f(n) = O(n^2)$

$\log_b(a) = \log_2(8) = 3 > 2$.

Thus,

$$
T(n) = \Theta(n^{\log_b(a)}) = \Theta(n^3)
$$

2. $T(n) = 2T(n/2) + 10n$

$a=2, b-2, c=1, f(n) = 10n$

$f(n) = \Theta(n^c \log^k n)$, where $c=1, k=0$

$\log_b a = \log_2 2 = 1$, therefore, $c = \log_b a$

$T(n) = \Theta(n^{\log_b a} \log^{k+1} n) = \Theta(n \log n)$

3. $T(n) = 2T(n/2) + n^2$

$a=2, b=2, f(n) = n^2$

$f(n) = \Omega(n^c)$, where $c=2$.

Filling case 3 condition:

$\log_b a = \log_2 1$, so $c > \log_b a$.

Regularity condition:

$2 n^2 / 4 \leq kn^2$, choosing $k = 1/2$.

So:

$T(n) = \Theta(n^2)$.
